import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread(cv.samples.findFile("groundtruth-rot0-2.png"))
if img is None:
    sys.exit("Could not read the image.")

# Using resize to decrease the size of the image
scale_percent = 20 # percent of original size
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dim = (width, height)
img = cv.resize(img, dim)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of color in HSV
lower = np.array([0,0,255])
upper= np.array([255,255,255])

# Threshold the HSV image to get only blue colors
mask = cv.inRange(hsv, lower, upper)

# Bitwise-AND mask and original image
res = cv.bitwise_and(img,img, mask= mask)

plt.subplot(131),plt.imshow(img),plt.title('image')
plt.subplot(132),plt.imshow(mask),plt.title('mask')
plt.subplot(133),plt.imshow(res),plt.title('res')

plt.show()

