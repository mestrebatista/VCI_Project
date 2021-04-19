import numpy as np
import cv2 as cv

videoCaptureObject = cv.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    cv.imwrite("NewPicture.jpg",frame)
    result = False
videoCaptureObject.release()
cv.destroyAllWindows()