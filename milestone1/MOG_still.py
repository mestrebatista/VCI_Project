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

cv.imshow('frame',fgmask)
k = cv.waitKey(0) & 0xff


cap.release()
cv.destroyAllWindows()

# mog2 melhor para imagens!

