import cv2.cv2 as ocv
import numpy as np
import os

imgpath = "D:\\Documents\\Programs\\Images"
classif = ocv.CascadeClassifier("D:\\Documents\\Programs\\haarcascade_frontalface_default.xml")

for img_f in os.listdir(imgpath):
    try:
        # Read each file into an image
        print(img_f)
        img = ocv.imread(imgpath + '\\' + img_f)

        faces = classif.detectMultiScale(img, scaleFactor=1.5, minNeighbors=5)

        count = 0
        for (x, y, w, h) in faces:
            # As img is really a NumPy object
            roi = img[y:y+h, x:x+w]
            ocv.imwrite("D:\\Documents\\Programs\\Cropped\\" + img_f[:-4] + "_cr" + str(count) + ".jpg", roi)
    except:
        continue