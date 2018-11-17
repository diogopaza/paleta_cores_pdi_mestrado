import cv2
import numpy as np
import unittest

# 0: red   60:green  120:blue  180: red
HUE = 0
GRAYSCALE = 0

DEFAULT_SATURATION = 180     # valor default para saturation
DEFAULT_VALUE = 180		# valor default para valor

PALET_WIDTH = 200

def generate_palette(hue1, hue2):
	h = np.linspace(hue1, hue2, 256)
	s = np.tile(DEFAULT_SATURATION, 256) # saturation fixed
	i = np.tile(DEFAULT_VALUE, 256) # value fixed

	p1 = np.tile(h.reshape((256,1)), PALET_WIDTH)
	p2 = np.tile(s.reshape((256,1)), PALET_WIDTH)
	p3 = np.tile(i.reshape((256,1)), PALET_WIDTH)

	p1 = np.uint8(p1)
	p2 = np.uint8(p2)
	p3 = np.uint8(p3)

	palet = np.dstack((np.dstack((p1, p2)), p3))
	return palet

def start(filename, hue1, hue2):
	img = cv2.imread(filename, GRAYSCALE)

	palet = generate_palette(hue1, hue2)
	colors = palet[:, 0]
	img = colors[img]

	bgr_img = cv2.cvtColor(img, cv2.COLOR_HSV2BGR)
	bgr_paleta = cv2.cvtColor(palet, cv2.COLOR_HSV2BGR)

	# RESULTADOS
	cv2.imshow('imagem', bgr_img)
	cv2.imshow('paleta', bgr_paleta)

	cv2.waitKey(0)
	cv2.destroyAllWindows()


filename = "militar.jpg"
hue1 = 0
hue2 = 200

start(filename, hue1, hue2)
