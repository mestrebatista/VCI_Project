from picamera import PiCamera
from time import sleep
import cv2 as cv
import functionTest as function
from pyimagesearch.centroidtracker import CentroidTracker
import Measure

cap =cv.VideoCapture(0)

x = 1

while True:
    
    frame = cap.read()
    frame = frame[1]

    frame=function.imageResize(frame)
    edges = function.backroundSub(cap)
    frame, contours = function.contour(frame, edges)
    frame = Measure.getMeasure(frame, contours)

    if x == 1:
        # set a centroid tracker
        ct = CentroidTracker()
        x = 0

    frame=function.objectTracking(frame, ct)
    cv.imshow("frame", frame)
    
    
    if cv.waitKey(1) == ord('q'):
        cap.release()
        cv.destroyAllWindows()
        break

cv.destroyAllWindows()
