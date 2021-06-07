import function
import cv2 as cv
import numpy as np
import Measure
from matplotlib import pyplot as plt

img = cv.imread("legoPictures/Legos4.jpg")
background = cv.imread("legoPictures/Background.jpg")

#resise images and background
#img = function.imageResize(img)
#background=function.imageResize(background)
#color(função usada mas nao aplicada posteriormente)
color = function.colorDetection(img)
#edges
edges = function.backroundSub(background, img)
#contourns
img, contours = function.contour(img, edges)
#measure
#img=Measure.getMeasure(img,contours)

#object tracking and id
img=function.objectTracking(img)
cv.imshow('contours', img)
cv.waitKey(0) & 0xFF

