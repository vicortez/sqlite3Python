import cv2
import numpy as np
import matplotlib.pyplot as plt

img1 = cv2.imread('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\foto.png')
img2 = cv2.imread('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\lena.tiff')
rols, cols, channels = img1.shape
img2b = img2[0:rols,0:cols]

add = img1 + img2b

img2[0:rols,0:cols]=add

cv2.imshow('foto',img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

