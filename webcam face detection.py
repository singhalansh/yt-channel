import cv2
from cv2 import VideoCapture


face= cv2.CascadeClassifier("D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml")

# capturing video
fourcc = cv2.VideoWriter_fourcc(*'XVID') # type: ignore
# out = cv2.VideoWriter('face_out.avi',fourcc,20.0,(720,720))
cap= VideoCapture(0)

while 1:
    ret,img=cap.read()
    
    gray  = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    # out.write(img)
    
    # detecting faces with the image
    # detectMultiscale(image,scaling factor,min neighbours(min num of images needed to match the face),minimum size of face)
    faces = face.detectMultiScale(gray,1.1,6,minSize=(100,60))

    # drawing rectangle around the face
    for (x,y,w,h) in faces:
        # cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)
        a=int(x+(w/2))
        b=int(y+(h/2))
        cv2.circle(img,(a,b),100,(0,155,25),2)

    # showing found faces
    cv2.imshow("faces in image",img)
    k = cv2.waitKey(10) & 0xff
    if k==27:
        break
    
cap.release()
# out.release()

cv2.destroyAllWindows()