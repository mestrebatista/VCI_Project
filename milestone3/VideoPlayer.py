import numpy as np
import cv2 as cv
import functionVideo as function
import time
from pyimagesearch.centroidtracker import CentroidTracker
import Measure


ct = CentroidTracker()
(H, W) = (None, None)

cap = cv.VideoCapture("video4.h264")


frame = cap.read()
frame = frame[1]


# cv.imwrite("background.jpg", frame)
# background=cv.imread("background.jpg")
# #background = cv.GaussianBlur(background, (5, 5), 0)
# background=function.imageResize(background)

if W is None or H is None:
	(H, W) = frame.shape[:2]




while True:
    frame = cap.read()
    frame = frame[1]
    frame = cv.flip(frame, -1) # inverter video
    if W is None or H is None:
        (H, W) = frame.shape[:2]

    frame=function.imageResize(frame)
    #frame = cv.GaussianBlur(frame, (5, 5), 0)
    edges = function.backroundSub(cap)
    frame, contours = function.contour(frame, edges)
    frame = Measure.getMeasure(frame, contours)

    frame=function.objectTracking(frame)
    cv.imshow("frame", frame)

    if cv.waitKey(1) == ord('q'):
        break

cv.destroyAllWindows()
#cap.stop()