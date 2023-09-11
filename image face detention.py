#importing libraries
import cv2
import numpy as np
#loading cascade
face = cv2.CascadeClassifier("D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

#reading an image
#cv2.imread(pah,flag)
image=cv2.imread("test.jpg")

#converting to grayscale as contains less noise
#cvtcolor(image,conversion code,output file,...)
gray = cv2.cvtColor(image,cv2.COLOR_RGB2BGR)

# detecting faces with the image
# detectMultiscale(image,scaling factor,min neighbours(min num of images needed to match the face),minimum size of face)
faces = face.detectMultiScale(gray,1.1,4,minSize=(100,60))

# drawing rectangle around the face
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),1)
    
# printing number of 
print("faces found : ",len(faces))

# showing found faces
cv2.imshow("faces in image",image)
cv2.waitKey()