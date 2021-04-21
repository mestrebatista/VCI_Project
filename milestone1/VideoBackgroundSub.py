import numpy as np
import cv2 as cv


cap = cv.VideoCapture('vtest.avi')

fgbg = cv.bgsegm.createBackgroundSubtractorMOG()   #mog já não está nos modulos do onpencv pelo que são necessátios modulos extra
													#pip install opencv-contrib-python

#fgbg = cv.createBackgroundSubtractorMOG2()		#algoritmo mog2       

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv.imshow('frame',fgmask)
    k = cv.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv.destroyAllWindows()

# com a amostra de video testada mog1, mesmo num comptador de grande capacidade de processamento, parece apresentar melhores resultados ao contrario do que seriam as expetativas!