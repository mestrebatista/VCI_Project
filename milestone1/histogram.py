import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt


# alterar codigo para suportar video input

img = cv.imread('messi5.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)# img to gray
cv.imshow('image1',gray)
cv.namedWindow('image1', cv.WINDOW_AUTOSIZE)
grey_hist=cv.calcHist([gray.ravel()],[0],None,[256],[0,256])
plt.plot(grey_hist)
plt.show()


hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # img to HSV
cv.imshow('image2',hsv)
cv.namedWindow('image2', cv.WINDOW_NORMAL)
hsv_hist=cv.calcHist([hsv.ravel()],[0],None,[256],[0,256])
plt.plot(hsv_hist)
plt.show()

yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)  # img to YUV
cv.imshow('image3',yuv)
cv.namedWindow('image3', cv.WINDOW_NORMAL)
yuv_hist=cv.calcHist([yuv.ravel()],[0],None,[256],[0,256])
plt.plot(yuv_hist)
plt.show()

cv.waitKey(0)
cv.destroyAllWindows()