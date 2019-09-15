import os, uuid, sys
import numpy as np
import time
from azure.storage.blob import BlockBlobService, PublicAccess
n_array = range(2, 103)

def get_file_path(n):
    local_path = os.path.expanduser("~/Pictures/sample")
    return os.path.join(local_path, get_file_name(n))

def get_file_name(n):
    num_zeros = int(5 - np.floor(np.log10(n)))
    local_file_name = "write_" + num_zeros*"0" + str(n) + ".png"
    return local_file_name

def get_download_path(n):
    return os.path.join(os.path.expanduser("~/Pictures/target"), get_file_name(n))

def upload_file(dir, service, bn, name):
    try:
        service.create_blob_from_path(bn, name, dir)
    except Exception as e:
        print(e)

def run_sample():
    try:
        # Create the BlockBlockService that is used to call the Blob service for the storage account
        block_blob_service = BlockBlobService(account_name='htn2019', account_key='1jvcfmZQrfPUSZdv8Ofdv3L7047OkmMfY66ZEeYYSf3DFMF+kia/5qzO68UsX8fL4utjCq1iTOUQdHIVdbciTQ==')

        # Create a container called 'container'.
        container_name ='container'
        block_blob_service.create_container(container_name)

        # Set the permission so the blobs are public.
        block_blob_service.set_container_acl(container_name, public_access=PublicAccess.Container)

        # Main Loop
        start = time.time()
        for i in n_array:
            file_name = get_file_name(i)
            print("Uploading: " + file_name)
            # Upload file
            block_blob_service.create_blob_from_path(container_name, get_file_name(i), get_file_path(i))

        print("Done. Time elapsed: " + str(time.time() - start))

        # List the blobs in the container
        print("\nList blobs in the container")
        generator = block_blob_service.list_blobs(container_name)
        for blob in generator:
            print("\t Blob name: " + blob.name)
            print(str(block_blob_service.make_blob_url(container_name, blob.name)))


        # Download the blob(s).
        # Add '_DOWNLOADED' as prefix to '.txt' so you can see both files in Documents.
        start2 = time.time()
        for i in n_array:
            target = get_download_path(i)
            file_name = get_file_name(i)
            print("Downloading: " + file_name)
            block_blob_service.get_blob_to_path(container_name, file_name, target)
        print("Done. Time elapsed: " + str(time.time() - start2))

        # Clean up resources. This includes the container and the temp files
        sys.stdout.write("Sample finished running. When you hit <any key>, the sample will be deleted and the sample "
                         "application will exit.")
        sys.stdout.flush()
        input()

        block_blob_service.delete_container(container_name)
        folder = "~/Pictures/target"
        for the_file in os.listdir(folder):
            file_path = os.path.join(folder, the_file)
            try:
                if os.path.isfile(file_path):
                    os.unlink(file_path)
                # elif os.path.isdir(file_path): shutil.rmtree(file_path)
            except Exception as e:
                print(e)

    except Exception as e:
        print(e)



# Main method.
if __name__ == '__main__':
    run_sample()



