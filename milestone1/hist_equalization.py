import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

def hist_eq(picture):
    img = cv.imread(picture)

    #CLAHE object
    clahe = cv.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
    cl1 = clahe.apply(img)
    #cl1 = cv.equalizeHist(img)
    cv.imwrite('clahe_2.png',cl1)

    #cap.release()
    cv.destroyAllWindows()
hist_eq("legoImage.png")


