import numpy as np
import cv2

#imagens com tamanhos iguais
img1 = cv2.imread('C:\\Users\\USER\\Google Drive\\Profissional - academico\\Programas\\phyton\\3d.png')
img2 = cv2.imread('C:\\Users\\USER\\Google Drive\\Profissional - academico\\Programas\\phyton\\svm.png')
img = cv2.imread('C:\\Users\\USER\\Google Drive\\Profissional - academico\\Programas\\phyton\\mainlogo.png')

#soma a imagem, nao é o melhor jeito
#add = img1 + img2

#soma o valor de cada cor de cada pixel
#add = cv2.add(img1,img2)

#METODO QUE PRESTA ultimo = gamma
weighted = cv2.addWeighted(img1,0.6,img2,0.4,0)

#pegamos o numero de linhas e colunas da imagem menor
rols, cols, channels = img.shape
#definimos roi como sendo de 0,0 ate o tamanho de img na figura img1
roi = img1[0:rols,0:cols]

#mask of the logo
imgtogray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#qualquer valor acima de threshold 220 sera convertido para 255. se esta abaixo, é convertido para 0,
#aqui invertemos o efeito.
ret,mask = cv2.threshold(imgtogray,220,255,cv2.THRESH_BINARY_INV)

#cv2.imshow('mask',mask)
#cv2.imshow('unmasked',img)

#inverte os valores de mask
mask_inv= cv2.bitwise_not(mask)

img1_background = cv2.bitwise_and(roi,roi,mask=mask_inv)

img_foreground = cv2.bitwise_and(img,img,mask=mask)

dst = cv2.add(img1_background, img_foreground)

roi = img1[0:rols,0:cols] = dst

# cv2.imshow('rest',img1)
# cv2.imshow('img1bg',img1_background)
# cv2.imshow('img',img)
# cv2.imshow('imgfg',img_foreground)
# cv2.imshow('mask',mask)
# cv2.imshow('maskinv',mask_inv)
# cv2.imshow('dst',dst)


cv2.imshow('weighted',weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()