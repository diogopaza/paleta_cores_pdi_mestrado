import cv2
import numpy as np
from matplotlib import pyplot as plt

#importa a imagem original em tons de cinza passando parametro 0
img = cv2.imread("militar.jpg",0)
minha_img = img
SV=180
PALETA=200

#Função para gerar uma paleta de cores com início e fim
def criar_paleta(inicio, fim):


    #Gera vetor entre inicio e fim com 256 posições
    h=np.linspace(inicio, fim,256)
    s=np.tile(SV,256)
    i=np.tile(SV,256)

    #Dando nova forma ao array
    novoH=np.tile(h.reshape((256,1)), PALETA)
    novoS=np.tile(s.reshape((256,1)), PALETA)
    novoI=np.tile(i.reshape((256,1)), PALETA)

    #converte para 8bits
    novoH=np.uint8(novoH)
    novoS=np.uint8(novoS)
    novoI=np.uint8(novoI)
    #unindo os vetores para gerar a paleta
    minhaPaleta = np.dstack((np.dstack((novoH,novoS)), novoI))
    return minhaPaleta

#criando nova imagem com 3 canais 
img2=np.zeros( (img.shape[0], img.shape[1],3 ))

#gera paleta HSI
paleta = criar_paleta(0,60)


#percorrendo cores
cores_paleta=paleta[:,0]
img=cores_paleta[img]

bgr_img=cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
bgr_paleta=cv2.cvtColor(paleta, cv2.COLOR_HSV2BGR)

cv2.imwrite("paleta.jpg", bgr_paleta)

#imagens finais
cv2.imshow("original", minha_img)
cv2.imshow("paleta", bgr_paleta)
cv2.imshow("Imagem de Saida", bgr_img)






