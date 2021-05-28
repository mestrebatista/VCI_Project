import cv2 as cv
import numpy as np
import function
import Measure

img=cv.imread("groundtruth-rot0-2.png")
img = function.imageResize(img) #resize the original image

#convert image: blur it
#blur the image for better edge detection
imgBlur=cv.GaussianBlur(img,(7,7),0)

#find edges in the images using Canny
imgCanny=cv.Canny(imgBlur,50,50)
#get contours of the edges in the image
imgContour=Measure.getMeasure(img, imgCanny)


#show results
#cv.imshow("original",img)
#cv.imshow("Blur",imgBlur)
cv.imshow("Edges",imgCanny)
cv.imshow("Contours",imgContour)
cv.waitKey(0)
