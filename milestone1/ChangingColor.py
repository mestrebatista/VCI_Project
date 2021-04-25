import cv2 as cv
import numpy as np

def imageResize(image):

    # Percent of original size
    scale_percent = 15

    # Width
    width = int(image.shape[1] * scale_percent / 100)
    # Height
    height = int(image.shape[0] * scale_percent / 100)

    # Dimensions
    dim = (width, height)

    # Resizes the image with the new dimensions
    resizedImage = cv.resize(image, dim)

    # Returns the image resized
    return resizedImage


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

# Bitwise-AND mask and original image
res1 = cv.bitwise_and(img, img, mask= mask1)
res2 = cv.bitwise_and(img, img, mask= mask2)
res3 = cv.bitwise_and(img, img, mask= mask3)

img = imageResize(img)
res1 = imageResize(res1)
res2 = imageResize(res2)
res3 = imageResize(res3)
while(1):
    cv.imshow("Range of Blue", res1)
    cv.imshow("Range of Green", res2)
    cv.imshow("Range of Red", res3)
    cv.imshow("Original Image", img)
    if cv.waitKey(20) & 0xFF == 27:
        break

cv.destroyAllWindows()