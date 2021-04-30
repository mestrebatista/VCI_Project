import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def hist(picture):

    img = cv.imread(picture) #adquire a imagem do vídeo

    #tratamento da imagem original
    cv.imshow('image1',img)
    cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
    origin_hist=cv.calcHist([img],[0],None,[256],[0,256])
    plt.plot(origin_hist)
    plt.show()

    # tratamento da imagem para escala HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # img to HSV
    cv.imshow('image2',hsv)
    cv.namedWindow('image2', cv.WINDOW_NORMAL)
    hsv_hist=cv.calcHist([hsv.ravel()],[0],None,[256],[0,256])
    plt.plot(hsv_hist)
    plt.show()

    # tratamento da imagem para escala cinzenta
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)# img to gray
    cv.imshow('image1',gray)
    cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
    grey_hist=cv.calcHist([gray.ravel()],[0],None,[256],[0,256])
    plt.plot(grey_hist)
    plt.show()

    cv.waitKey(0)
    cv.destroyAllWindows()
