import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import Measure

def contour1(image):
    #image = cv.imread(img)
    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    ret, thresh = cv.threshold(imgray, 0, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0,255,0), 6)


    #img = image.imageResize(image)
    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
    cv.imshow('Display', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image,contours


def contour2(image, imgray):
    ret, thresh = cv.threshold(imgray, 0, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    cv.drawContours(image, contours, -1, (0,255,0), 6)

    cv.imshow('Display', image)
    cv.waitKey(0)
    cv.destroyAllWindows()
    return image,contours

def colorDetection(img):

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([112, 220, 50])
    upper_blue = np.array([120, 255, 255])

    # define range of green color in HSV
    lower_green = np.array([50, 100, 100])
    upper_green = np.array([105, 255, 255])

    # define range of red color in HSV
    lower_red = np.array([150, 155, 0])
    upper_red = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    mask3 = cv.inRange(hsv, lower_red, upper_red)
    mask = mask2     # + mask2 + mask3;

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(img, img, mask=mask)

    # Changing Colors to RGB in  order to do the plot
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    res = cv.cvtColor(res, cv.COLOR_BGR2RGB)
    mask = cv.cvtColor(mask, cv.COLOR_BGR2RGB)

    res = imageResize(res)
    #cv.imwrite("img_new.jpg", res)

    plt.subplot(1, 3, 1), plt.imshow(img), plt.title('Original Image')
    plt.subplot(1, 3, 2), plt.imshow(res), plt.title('Range of Blue, Green and RED')
    plt.subplot(1, 3, 3), plt.imshow(mask), plt.title('Mask')
    plt.show()

    return res

def imageResize(image):

    # Percent of original size
    scale_percent = 100

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


def backroundSub(background, img):

    fgbg = cv.bgsegm.createBackgroundSubtractorMOG()

    fgmask = fgbg.apply(background)


    fgmask = fgbg.apply(img)

    edges = cv.Canny(fgmask, 100, 200)

    cv.imshow('edges',edges)
    k = cv.waitKey(0) & 0xff

    return edges


img = cv.imread("legoPictures/Legos10.jpg")
background = cv.imread("legoPictures/Background.jpg")
img = imageResize(img)
edges = backroundSub(background, img)
img, contours = contour2(img, edges)

color = colorDetection(img)