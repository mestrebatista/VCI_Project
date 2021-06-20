import cv2 as cv
import functionVideo as function
from pyimagesearch.centroidtracker import CentroidTracker
import Measure


ct = CentroidTracker()
(H, W) = (None, None)

cap = cv.VideoCapture("video4.h264")


frame = cap.read()
frame = frame[1]

if W is None or H is None:
	(H, W) = frame.shape[:2]

x = 1

while True:
    frame = cap.read()
    frame = frame[1]
    frame = cv.flip(frame, -1) # inverter video
    if W is None or H is None:
        (H, W) = frame.shape[:2]

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
        break

cv.destroyAllWindows()
