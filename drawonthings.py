import numpy as np
import cv2

# img = cv2.imread('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\cores.png',cv2.IMREAD_COLOR)
# lin,col,can=img.shape
# print('lin = ',lin,'col = ',col)
# img[0:9,0:9]=(0,0,0)
# img[10:19,0:10]=(255,255,255)
# img[20:29,0:10]=(0,0,0)
# img[0:9,10:19]=(0,255,0)
# img[0:9,20:29]=(0,0,255)
# img[10:19,10:19]=(100,50,0)
# img[10:19,20:29]=(60,10,100)
#
# roi1 = img[10:19,0:10]
# roi2 = img[20:29,0:10]
# add = roi1 + roi2
#
# print(add[0:9,0:9])
#
# cv2.imshow('1',roi1)
# cv2.imshow('2',roi2)
# cv2.imshow('add',add)
#
# cv2.imshow('foto',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
#



img = cv2.imread('C:\\Users\\victo\\Google Drive\\Profissional - academico\\Programas\\phyton\\Lena.tiff',cv2.IMREAD_COLOR)


cv2.ellipse(img,(300,300),(100,100),90,0,180,255,-1)

#BGR
cv2.line(img, (0,0), (100,100), (255,0,0), 10)

cv2.rectangle(img, (80,80), (200,250),(0,255,0), 5)

#line thikness =-1 preenche
cv2.circle(img, (200,200), 100, (0,0,255), 5,cv2.LINE_AA)

pts = np.array([[250,350],[300,250],[150,200],[50,100],[30,90]], np.int32)
#pts = pts.reshape((-1,1,2))

#true = conectar o ultimo e o primeiro ponto
cv2.polylines(img,[pts], True, (0,255,255), 3,cv2.LINE_AA)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'openCV eh aquela coisa', (100,300),font,1,(255,255,255),2,cv2.LINE_AA)

cv2.imshow('img',img)

cv2.waitKey(0)
cv2.destroyAllWindows()