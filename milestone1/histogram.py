import numpy as np
import cv2 as cv
#import matplotlib.image as mpimg
from matplotlib import pyplot as plt

def hist(picture):

    img = cv.imread(picture)  # adquire a imagem do vídeo

    # juntar tudo na mesma imagem
    plt.figure(1)
    plt.subplot(221)
    plt.title('Original Image')
    # tratamento da imagem original
    plt.imshow(img)

    plt.subplot(222)
    plt.title('Original Image Histogram')
    origin_hist = cv.calcHist([img], [0], None, [256], [0, 256])
    plt.plot(origin_hist)

    # tratamento da imagem para escala HSV
    plt.subplot(223)
    plt.title('HSV Image')
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # img to HSV
    plt.imshow(hsv)

    plt.subplot(224)
    plt.title('HSV Image Histogram')
    hsv_hist = cv.calcHist([hsv.ravel()], [0], None, [256], [0, 256])
    plt.plot(hsv_hist)
    plt.show()

hist("groundtruth-rot0-2.png")
