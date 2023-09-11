import cv2
import numpy as np

face = cv2.CascadeClassifier(
    "D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml"
)
eyes = cv2.CascadeClassifier(
    "D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_eye.xml"
)
smile = cv2.CascadeClassifier(
    "D:\\python3\\Lib\\site-packages\\cv2\\data\\haarcascade_smile.xml"
)


cap = cv2.VideoCapture(0)

while 1:
    r, img = cap.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    faces = face.detectMultiScale(gray, 1.1, 6, minSize=(100, 60))

    # drawing rectangle around the face
    for x, y, w, h in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # cv2.circle(img,(x,y),100,(0,155,25))
        region_of_interest_gray = gray[y : y + h, x : x + w]
        region_of_interest_color = img[y : y + h, x : x + w]

        eye = eyes.detectMultiScale(region_of_interest_gray, 1.1, 3)
        for ex, ey, ew, eh in eye:
            cv2.rectangle(
                region_of_interest_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2
            )

        smiles = smile.detectMultiScale(region_of_interest_gray, 1.4, 5)
        for sx, sy, sw, sh in smiles:
            cv2.rectangle(
                region_of_interest_color, (sx, sy), (sx + sw, sy + sh), (0, 0, 255), 2
            )

    # showing found faces
    cv2.imshow("faces in image", img)
    k = cv2.waitKey(30) & 0xFF
    if k == 27:
        break

cap.release()
# out.release()

cv2.destroyAllWindows()
