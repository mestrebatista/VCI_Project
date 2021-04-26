import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('messi5.jpg',0)

#CLAHE object
clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
cl1 = clahe.apply(img)
#cl1 = cv.equalizeHist(img)
cv.imwrite('clahe_2.png',cl1)




