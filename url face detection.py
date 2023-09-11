#importing libraries

import cv2
import numpy as np
import urllib.request
#loading cascade
face = cv2.CascadeClassifier("D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# opening url
# url = "https://www.amazon.in/BIRDS-MIND-Synthetic-Hanging-Poster/dp/B0974JNY88.jpg"
url="https://photosfile.com/wp-content/uploads/2022/02/Shri-Ram-5.jpg"
req = urllib.request.Request(url=url,headers={'User-Agent':'mozilla/5.0'})
urlresponse = urllib.request.urlopen(req)
# url to image array
image_array = np.array(bytearray(urlresponse.read()),dtype=np.uint8)
img = cv2.imdecode(image_array,-1)
#reading an image
#cv2.imread(pah,flag)
image=cv2.imread("test.jpg")

#converting to grayscale as contains less noise
#cvtcolor(image,conversion code,output file,...)
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# detecting faces with the image
# detectMultiscale(image,scaling factor,min neighbours(min num of images needed to match the face),minimum size of face)
faces = face.detectMultiScale(gray,1.1,4,minSize=(100,60))

# drawing rectangle around the face
for (x,y,w,h) in faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0, 255, 37),2)
    
# printing number of 
print("faces found : ",len(faces))

# showing found faces
cv2.imshow("faces in image",img)
cv2.waitKey()