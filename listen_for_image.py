# Listens for an image put into a file and uploads it
from pathlib import Path

import time
from azure.storage.blob import BlockBlobService, PublicAccess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

block_blob_service = BlockBlobService(account_name='htn2019', account_key='1jvcfmZQrfPUSZdv8Ofdv3L7047OkmMfY66ZEeYYSf3DFMF+kia/5qzO68UsX8fL4utjCq1iTOUQdHIVdbciTQ==')
blob_name = "captures"
j = 0
n = 7

class Watcher:
    dir = "./images"

    def __init__(self):
        self.observer = Observer()

    def run(self):
        event_handler = Handler()
        self.observer.schedule(event_handler, self.dir, recursive=True)
        self.observer.start()
        try:
            while True:
                time.sleep(5)
        except:
            self.observer.stop()
            print("Error")

        self.observer.join()


class Handler(FileSystemEventHandler):

    @staticmethod
    def on_any_event(event):
        if event.is_directory:
            return None
        elif event.event_type =='created':
            global j
            if j <= 6:
                j += 1
            else:
                j = 0
            image_name = "g" + str(j) + ".jpg"

            # Take any action here when a file is first created.
            print("Received created event - $s." + str(event.src_path))
            block_blob_service.create_blob_from_path("captures", "t" + str(i), event.src_path)
            # upload_file(event.src_path, block_blob_service, blob_name, image_name)
            # block_blob_service.get_blob_to_path(blob_name, os.path.basename(event.src_path),
            #                                     os.path.join(os.path.expanduser("~/Pictures/target"), os.path.basename(event.src_path)))
            # print(str(block_blob_service.make_blob_url(blob_name, os.path.basename(event.src_path))))
        # elif event.event_type == 'modified':
            # Taken any action here when a file is modified.

def upload_7():
    for i in range(n):
        upload_file("/home/sniprs/anaconda3/envs/storage-blobs-python-quickstart/gallery/g" + str(i) + ".jpg", block_blob_service, "gallery")
        print(str(block_blob_service.make_blob_url("gallery", "g" + str(i))))

def watch_for_stuff():
    w = Watcher()
    w.run()