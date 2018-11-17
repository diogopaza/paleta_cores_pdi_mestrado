import cv2
import numpy as np
import unittest

#importa a imagem original em tons de cinza passando parametro 0
img = cv2.imread("militar.jpg",0)
#cv2.imshow("original", img)

#criando nova imagem com 3 canais 
img2=np.zeros( (img.shape[0], img.shape[1],3 ))


print(img2.shape)
"""
h=np.linspace(0,60,256)
s=np.tile(DEFAULT_SATURATION,256)
print(s)
"""
