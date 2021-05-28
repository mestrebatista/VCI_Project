import cv2 as cv
import numpy as np


#def getContours(img, imgCanny):
def getMeasure(img,contours):
    #contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    imgCopy = img.copy()
    for cnt in contours:
        area = cv.contourArea(cnt + 1)
        print("Area:", area)  # area
        if area < 7900 and area>30:
            imgContour = cv.drawContours(imgCopy, cnt, -1, (0, 255, 0), 2)
            perimetro = cv.arcLength(cnt, True)
            print("Per:",perimetro)  # perimetro
            cornerPoints = cv.approxPolyDP(cnt, 0.02 * perimetro, True)
            numCorners = len(cornerPoints)
            print("Cantos:",numCorners)  # numero de vértices
            x, y, w, h = cv.boundingRect(cornerPoints)

            if numCorners == 4:
                aspRatio=w/float(h)
                if aspRatio>0.30 and aspRatio<1.70:
                    LegoType="Pequeno"
                elif aspRatio>0 and aspRatio<2:
                    LegoType="Medio"
                else:
                    LegoType="Grande"
            else: LegoType = "None"

            cv.rectangle(imgCopy,(x,y),(x+w,y+h),(255,0,0),2)
            cv.putText(imgCopy,LegoType,(x+(w//4)-30,y+(h)+20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),1)

    cv.imshow("Contours", imgCopy)
    cv.waitKey(0)
    cv.destroyAllWindows()


    return imgContour
