import numpy as np
import cv2 as cv



#fgbg = cv.bgsegm.createBackgroundSubtractorMOG()   #mog já não está nos modulos do onpencv pelo que são necessátios modulos extra
													#pip install opencv-contrib-python

fgbg = cv.createBackgroundSubtractorMOG2()		#algoritmo mog2

image1 = cv.imread('fundo.jpg')
image2 = cv.imread('legoImage.png')       


#ret, frame = cap.read()

fgmask = fgbg.apply(image1)

cv.imshow('frame',fgmask)
k = cv.waitKey(30) & 0xff



fgmask = fgbg.apply(image2)

edges = cv.Canny(fgmask,100,200)
cv.imshow('frame',fgmask)
cv.imshow('edges',edges)
k = cv.waitKey(0) & 0xff

contours, hierarchy = cv.findContours(edges, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
  
cv.imshow('Canny Edges After Contouring', edges)
k = cv.waitKey(0) & 0xff
  
print("Number of Contours found = " + str(len(contours)))

cv.drawContours(image2, contours, -1, (0, 255, 0), 3)
  
cv.imshow('Contours', image2)
k = cv.waitKey(0) & 0xff


cap.release()
cv.destroyAllWindows()