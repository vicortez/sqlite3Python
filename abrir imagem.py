# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 21:41:16 2016

@author: USER
"""

import cv2
import numpy as np
import matplotlib.pyplot as plt

#rbg alpha. escolhemos uma
# 0 = IMREAD_GRAYSCALE
# 1 = IMREAD_COLOR
# -1 = IMREAD_UNCHANGE
img=cv2.imread('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\foto.png',cv2.IMREAD_GRAYSCALE)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plotar usando o matplotlib.pyplot
#plt.imshow(img, cmap='gray',interpolation = 'bicubic')
#plt.plot([50,100],[100,50], 'g',linewidth=10)
#plt.show()
cv2.imwrite('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\fotob.png',img)