import numpy as np
import cv2 as cv


def hist_eq(picture):
    img = cv.imread(picture,0)

    #CLAHE object
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    #cl1 = cv.equalizeHist(img)
    cv.imwrite('Better_Image.png',cl1)

hist_eq("legoImage.png")


