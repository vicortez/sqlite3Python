# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:41:16 2016

@author: USER
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#se quisessemos capturar um video, substituir 0 pelo caminho do arquivo.
cap = cv2.VideoCapture(0)

#fourcc = codec FourCC is a 4-byte code used to specify the video codec. The list of available codes can be found in fourcc.org. It is platform dependent.
codecmeu = cv2.VideoWriter_fourcc(*'XVID')
out= cv2.VideoWriter('output.avi',codecmeu, 20.0, (640,480))
out2= cv2.VideoWriter('virado.avi',codecmeu, 20.0, (640,480))

while True:
   # capture frame by frame
    ret, frame = cap.read()

    if ret == True:
        framevirado = cv2.flip(frame, 0)
        out2.write(framevirado)


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    out.write(frame)

    cv2.imshow('fraime',frame)
    cv2.imshow('grayscale',gray)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

out.release()

cv2.destroyAllWindows()