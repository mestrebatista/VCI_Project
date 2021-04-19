import cv2 as cv
import sys
img = cv.imread(cv.samples.findFile("groundtruth-rot0-2.png"))
if img is None:
    sys.exit("Could not read the image.")

scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)

img = cv.resize(img, dim)

cv.imshow("Display window", img)
k = cv.waitKey(0)
cv.destroyAllWindows()