import numpy as np
import cv2 as cv


cap = cv.VideoCapture('vtest.avi')

fgbg = cv.bgsegm.createBackgroundSubtractorMOG()   #mog já não está nos modulos do onpencv pelo que são necessátios modulos extra
													#pip install opencv-contrib-python

#fgbg = cv.createBackgroundSubtractorMOG2()		#algoritmo mog2       

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    edges = cv.Canny(fgmask,100,200)
    #edges = cv.Canny(frame,100,200)
    cv.imshow('frame',fgmask)
    cv.imshow('edges',edges)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

# com a amostra de video testada, mesmo num comptador de grande capacidade de processamento, mog1 parece apresentar melhores resultados ao contrario do que seriam as expetativas!
