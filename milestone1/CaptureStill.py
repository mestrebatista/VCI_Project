import numpy as np
import cv2 as cv

videoCaptureObject = cv.VideoCapture(0)
result = True
while(result):
    ret,frame = videoCaptureObject.read()
    picture = cv.imwrite("NewPicture.jpg",frame)
    result = False

histogram.hist(picture)
videoCaptureObject.release()
cv.destroyAllWindows()