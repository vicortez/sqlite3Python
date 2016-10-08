import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('C:\\Users\\USER\\Google Drive\\Profissional - academico\\Programas\\phyton\\gameicon.png', cv2.IMREAD_COLOR)

#NA FORMA [LINHA, COLUNA]
img[0, 0] = [255,255,0]
img[1, 1] = [255,0,255]
img[0,1] = [0,0,0]

#px gaha o valor do pixel de coordenada 55,55 (array)
px = img[29,29]

print('px = ',px)
img[29,29] = [0,0,0]
print('new px = ',px)

px2 = img[29,28]
print('px2 = ',px2)


# accessing only blue pixel (0)
blue = img[0,0,0]
print ('valor blue[0,0,0] = ',blue)
#"mesma coisa" que:
print('valor em [0,0, cor 0]= ',img[0,0,0])

#red(2) of the same pixel:
print ('valor red[0,0,0] = ',img[0,0,2])



# accessing RED value 10,10
#jeito mais eficiente
print('valor vermelho em 10,10= ',img.item(10,10,2))

# modifying RED value [10,10] eficientemente
img.itemset((10,10,2),0)
print('novo valor vermelho 10,10= ',img.item(10,10,2))

#este processo pega até o pixel n-1
roi = img[0:2, 0:3]
print('roi = ',roi)
roi2 = img[3:5, 0:2] = [0,0,0]

img[3,0]=[255,0,0]
roi2 = img[3:5, 0:2]
print('roi2 = ',roi2)
print('0,1 = ',img[0,1])

#regiao recebe a matriz com linhas 250->350 e colunas 250->350
#regiao = img[250:350, 250:350]
#img recebe regiao no lugar dela nos pixels selecionados, tem que ser o mesmo tamanho l,c.
#img[0:100,411:511] = regiao

#acessar o numero de linhas, colunas e canais da imagem(se colorida)
#  --retorna um tuple entre parenteses, nao pode ser editado
print('img.shape retorna: ',img.shape)

#numero de pixels da imagem, 1pixel colorido conta como 3.
print('img.size: ',img.size)

#datatype (importate)
print('img.dtype: ',img.dtype)

#cv2.split divide a imagem em 3 imagens cada uma apenas com um valor: bgr
b,g,r = cv2.split(img)
cv2.imshow('blueimg',b)
b=img[:,:,0] #PASSAR SEM REFERENCIA DEPOIS
print('blue ',b)
img[:,:,0] = 0
print('blue dps ',b)
#se temos valores b, g e r modificados, podemos fundi-los numa imagem
danone = cv2.merge((b,g,r))

#Abaixo, bordas.
replicate = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REPLICATE)
reflect = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT)
reflect101 = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_REFLECT_101)
wrap = cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_WRAP)
constant= cv2.copyMakeBorder(img,30,30,30,30,cv2.BORDER_CONSTANT,value=[255,0,0])

plt.subplot(231),plt.imshow(img,'gray'),plt.title('ORIGINAL')
plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('REPLICATE')
plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('REFLECT')
plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('REFLECT_101')
plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('WRAP')
plt.subplot(236),plt.imshow(constant,'gray'),plt.title('CONSTANT')

plt.show()
#fim das bordas

cv2.imshow('danone',danone)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


