import function
import cv2 as cv

img = cv.imread("legoPictures/Legos1.jpg")
background = cv.imread("legoPictures/Background.jpg")

color = function.colorDetection(img)

#edges
edges = function.backroundSub(background, img)

#contourns
img, contours = function.contour(img, edges)

#object tracking and id
img=function.objectTracking(img)
cv.imshow('contours', img)
cv.waitKey(0) & 0xFF

