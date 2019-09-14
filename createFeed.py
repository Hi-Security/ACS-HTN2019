import cv2
import pickle
import datetime
import numpy as np
from imutils.video import VideoStream
import imutils
import os

class image_processor:

    def __init__(self):
        # face detector
        self.detector = cv2.dnn.readNetFromCaffe("deploy.prototxt", "res10_300x300_ssd_iter_140000.caffemodel")
        # data embedder that condenses the faces into the correct size vectors
        self.embedder = cv2.dnn.readNetFromTorch("openface_nn4.small2.v1.t7")

        # loads the custom created face recognizer into this variable
        self.recognizer = pickle.loads(open("output/recognizer.pickle", "rb").read())
        self.label_encode = pickle.loads(open("output/le.pickle", "rb").read())

    # cam = cv2.VideoCapture(0)
    # cam.set(cv2.CAP_PROP_FRAME_WIDTH,960)
    # cam.set(cv2.CAP_PROP_FRAME_HEIGHT,720)

    def findFaces(self,frame):
        # ret, frame = cam.read()
        timeinfo = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        cv2.putText(frame, timeinfo, (0, 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), thickness=2)

        try:
            frame = imutils.resize(frame, width=600)
        except AttributeError:
            print("no compatible webcam found")
            exit(0)
        h, w = frame.shape[:2]
        if frame.size == 0:
            return np.zeros(640,480)
        imageBlob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 1.0, (300, 300),
                                        (104.0, 177.0, 123.0), swapRB=False, crop=False)
        self.detector.setInput(imageBlob)
        detections = self.detector.forward()
        #
        for i in range(0, detections.shape[2]):
            confidence = detections[0, 0, i, 2]
            if (confidence >= 0.4):
                roi = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
                x1, y1, x2, y2 = roi.astype('int')

                detected_face = frame[y1:y2, x1:x2]
                face_height = abs(y1 - y2)
                face_width = abs(x1 - x2)

                if face_height < 25 or face_width < 25:
                    continue
                try:
                    faceBlob = cv2.dnn.blobFromImage(detected_face, 1.0 / 255, (96, 96), (0, 0, 0),
                                                    swapRB=True, crop=False)
                except:
                    continue

                self.embedder.setInput(faceBlob)
                vec = self.embedder.forward()

                prediction = self.recognizer.predict_proba(vec)[0]
                j = np.argmax(prediction)
                probaility = prediction[j]
                name = self.label_encode.classes_[j]

                text = "{}: {:.2f}%".format(name, probaility * 100)

                if y1 - 10 > 10:
                    Ylocation = y1 - 10
                else:
                    Ylocation = y1 + 10

                cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                cv2.putText(frame, text, (x1, Ylocation), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 0, 255), 2)

        return frame
        # if cv2.waitKey(20) == ord('q'):
        #     break

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)
    imporcess = image_processor()

    while True:
        ret,frame = cap.read()
        frame = imporcess.findFaces(frame)

        cv2.imshow("frame",frame)
        cv2.waitKey(1)
