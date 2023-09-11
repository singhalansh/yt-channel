#importing libraries
from tkinter.tix import Tree
import cv2
import numpy as np
#loading cascade
face = cv2.CascadeClassifier("D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

#reading an image

capture = cv2.VideoCapture("test vid.mp4")

if (capture.isOpened()==False):
    print("error")


while capture.isOpened():
    ret,image= capture.read()
    if ret == True:
        #converting to grayscale as contains less noise
        #cvtcolor(image,conversion code,output file,...)
        gray = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

        # detecting faces with the image
        # detectMultiscale(image,scaling factor,min neighbours(min num of images needed to match the face),minimum size of face)
        faces = face.detectMultiScale(gray,1.1,6,minSize=(100,60))

        # drawing rectangle around the face
        for (x,y,w,h) in faces:
            cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
            

        # showing found faces
        cv2.imshow("faces in image",image)
        k = cv2.waitKey(100)
        if k==27:
            break
capture.release()
cv2.destroyAllWindows()
