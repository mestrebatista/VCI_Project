import cv2 as cv
import numpy as np
import math


def getMeasure(img,contours):
    #contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    imgCopy = img.copy()
    for cnt in contours:
        area = cv.contourArea(cnt+1)
        print("Area:", area)  # area
        if area>1000:
            imgContour = cv.drawContours(imgCopy, cnt, -1, (0, 255, 0), 2)
            perimetro = cv.arcLength(cnt, True)
            #print("Per:",perimetro)  # perimetro
            cornerPoints = cv.approxPolyDP(cnt, 0.02 * perimetro, True)
            numCorners = len(cornerPoints)
            print("Cantos:",numCorners)  # numero de vértices
            x, y, w, h = cv.boundingRect(cornerPoints)

            unit_ref = 30
            ratio =[0,0]
            ratio[0] = int(round(w / (unit_ref)))          # width
            ratio[1] = int(round(h / (unit_ref)))           #height


    # Write the ratio on image
        cv.putText(imgCopy, str(ratio[0]) + "x" + str(ratio[1]), (x + w, y + h), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)

            # if numCorners == 4:
            #     aspRatio=w/float(h)
            #     if aspRatio>0.30 and aspRatio<1.70:
            #         LegoType="Pequeno"
            #     elif aspRatio>0 and aspRatio<2:
            #         LegoType="Medio"
            #     else:
            #         LegoType="Grande"
            # else: LegoType = "None"

            # cv.rectangle(imgCopy,(x,y),(x+w,y+h),(255,0,0),2)
            # cv.putText(imgCopy,LegoType,(x+(w//4)-30,y+(h)+20),cv.FONT_HERSHEY_SIMPLEX,0.7,(255,255,255),1)

    cv.imshow("Measures", imgCopy)
    cv.waitKey(0)
    cv.destroyAllWindows()


    return imgContour
