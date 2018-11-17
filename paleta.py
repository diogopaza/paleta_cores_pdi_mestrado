import cv2
import numpy as np
import unittest

#importa a imagem original em tons de cinza passando parametro 0
img = cv2.imread("militar.jpg",0)

SV=180
PALETA=250

#Função para gerar uma paleta de cores com início e fim
def criar_paleta(inicio, fim):


    #Gera vetor entre inicio e fim com 256 posições
    h=np.linspace(inicio, fim,256)
    s=np.tile(SV,256)
    i=np.tile(SV,256)
    print(s)

#criando nova imagem com 3 canais 
img2=np.zeros( (img.shape[0], img.shape[1],3 ))



criar_paleta(10,80)
