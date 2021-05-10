import numpy as np
import cv2 as cv


def hist_eq(picture):
    img = cv.imread(picture)

    #CLAHE object
    img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    img_yuv[:, :, 0] = clahe.apply(img_yuv[:, :, 0])
    img = cv.cvtColor(img_yuv, cv.COLOR_YUV2BGR)
    #creat new corrected image
    cv.imwrite('Better_Image1.png',img)



