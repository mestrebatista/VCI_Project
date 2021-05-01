import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import image
import histogram

img = cv.imread("groundtruth-rot0-2.png")

# Convert BGR to HSV
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

# define range of blue color in HSV
lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])

# define range of green color in HSV
lower_green = np.array([50,100,100])
upper_green = np.array([70,255,255])

# define range of red color in HSV
lower_red = np.array([0, 50, 120])
upper_red = np.array([10, 255, 255])

# Threshold the HSV image to get only blue colors
mask1 = cv.inRange(hsv, lower_blue, upper_blue)
mask2 = cv.inRange(hsv, lower_green, upper_green)
mask3 = cv.inRange(hsv, lower_red, upper_red)
mask = mask1+mask2+mask3;

# Bitwise-AND mask and original image
res = cv.bitwise_and(img, img, mask= mask)

res = image.imageResize(res)
cv.imwrite("img_new.jpg", res)

# Changing Colors to RGB in  order to do the plot
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
res = cv.cvtColor(res, cv.COLOR_BGR2RGB)
mask = cv.cvtColor(mask, cv.COLOR_BGR2RGB)

plt.subplot(1,3,1), plt.imshow(img), plt.title('Original Image')
plt.subplot(1,3,2), plt.imshow(res), plt.title('Range of Blue, Green and RED')
plt.subplot(1,3,3), plt.imshow(mask), plt.title('Mask')
plt.show()

histogram.hist("img_new.jpg")