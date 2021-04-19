import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("groundtruth-rot0-2.png"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("groundtruth-rot0-2.png", img)