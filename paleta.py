import cv2
import numpy as np
from matplotlib import pyplot as plt

#importa a imagem original em tons de cinza passando parametro 0
img = cv2.imread("militar.jpg",0)

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
imagem_colorida=np.zeros( (img.shape[0], img.shape[1],3 ))
imagem_cinza=img

#gera paleta HSI
paleta = criar_paleta(0,60)
cores_paleta=paleta[:,0]
img=cores_paleta[img]
for i in range(120,481,120):
    img_cores_paleta=cores_paleta[img[:i]]
    
print(img_cores_paleta.shape)

#percorrendo cores
cores_paleta=paleta[:,0]
img_cores_paleta=cores_paleta[img[:120]]
print(img.shape)
bgr_cinza=cv2.cvtColor(imagem_cinza, cv2.COLOR_GRAY2BGR)
bgr_img=cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
#saida=cv2.cvtColor(img_cores_paleta, cv2.COLOR_HSV2BGR)

#cv2.imwrite("paleta.jpg", bgr_paleta)

#imagens finais

#cv2.imshow("cinza", imagem_cinza)

#cv2.imshow("Imagem de Saida", bgr_img)
bgr_cinza[:120] =  bgr_img[:120]
cv2.imwrite("cinza_120.jpg", bgr_cinza)
bgr_cinza[:240] =  bgr_img[:240]
cv2.imwrite("cinza_240.jpg", bgr_cinza)
bgr_cinza[:360] =  bgr_img[:360]
cv2.imwrite("cinza_360.jpg", bgr_cinza)
bgr_cinza[:480] =  bgr_img[:480]
cv2.imwrite("cinza_480.jpg", bgr_cinza)


"""
for i in range(120,481,120):
    bgr_cinza[:i] =  bgr_img[:i]
    cv2.imwrite("atualizando", bgr_cinza)

#cv2.imshow("paleta",bgr_cinza )
"""




