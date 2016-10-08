import cv2

import cv2
from threading import Thread

cam = cv2.VideoCapture(0)
while True:
   # capture frame by frame
    ret, frame = cam.read()

    if ret == True:

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(gray, 100, 200)



    cv2.imshow('fraime',frame)
    cv2.imshow('grayscale',gray)
    cv2.imshow('edges', edges)



    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

out.release()

cv2.destroyAllWindows()