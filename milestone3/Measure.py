import cv2 as cv
import numpy as np
import math


def getMeasure(img,contours):
    #contours, hierarchy = cv.findContours(imgCanny, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_NONE)
    imgContour=img
    for cnt in contours:
        area = cv.contourArea(cnt+1)
        #print("Area:", area)  # area
        if area>2000:
            imgContour = cv.drawContours(img, cnt, -1, (0, 255, 0), 2)
            perimetro = cv.arcLength(cnt, True)
            #print("Per:",perimetro)  # perimetro
            cornerPoints = cv.approxPolyDP(cnt, 0.02 * perimetro, True)
            numCorners = len(cornerPoints)
            #print("Cantos:",numCorners)  # numero de vértices
            x, y, w, h = cv.boundingRect(cornerPoints)

            unit_ref = 30  # referencia de fotos
            #unit_ref = 15   #referencia de video
            ratio =[0,0]
            ratio[0] = int(round(w / (unit_ref)))          # width
            ratio[1] = int(round(h / (unit_ref)))           #height


            # Write the ratio on image
            cv.putText(img, str(ratio[0]) + "x" + str(ratio[1]), (x + w, y + h), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1, cv.LINE_AA)

    #cv.imshow("Measures", imgCopy)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return imgContour
