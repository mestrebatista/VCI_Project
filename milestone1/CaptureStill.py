import numpy as np
import cv2 as cv
import hist_equalization


videoCaptureObject = cv.VideoCapture(0)
result = True

while(result):
    ret,frame = videoCaptureObject.read()
    cv.imwrite("NewPicture.jpg",frame)
    result = False

hist_equalization.hist_eq("NewPicture.jpg")

videoCaptureObject.release()
cv.destroyAllWindows()

