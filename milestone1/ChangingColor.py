import cv2 as cv
import numpy as np
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

img = image.imageResize(img)
res = image.imageResize(res)
mask = image.imageResize(mask)

while(1):

    cv.imshow("Mask", mask)
    cv.imshow("Range of Blue, Green and RED", res)
    cv.imshow("Original Image", img)

    if cv.waitKey(20) & 0xFF == 27:
        cv.imwrite("img_new.jpg", res);
        cv.destroyAllWindows()
        break

histogram.hist("img_new.jpg")