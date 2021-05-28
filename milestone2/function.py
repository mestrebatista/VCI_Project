import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
import Measure

def contour(image):
    #img = cv.imread(image)
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

def colorDetection(img):

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])

    # define range of yellow color in HSV
    lower_yellow = np.array([20, 100, 100])
    upper_yellow = np.array([30, 255, 255])

    # define range of red color in HSV
    lower_red = np.array([0, 50, 120])
    upper_red = np.array([10, 255, 255])

    # Threshold the HSV image
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_yellow, upper_yellow)
    mask3 = cv.inRange(hsv, lower_red, upper_red)
    mask = mask1+mask2+mask3

    # Bitwise-AND mask and original image
    res = cv.bitwise_and(img, img, mask= mask)

    # Changing Colors to RGB in  order to do the plot
    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    res = cv.cvtColor(res, cv.COLOR_BGR2RGB)
    mask = cv.cvtColor(mask, cv.COLOR_BGR2RGB)

    res = imageResize(res)

    plt.subplot(1,3,1), plt.imshow(img), plt.title('Original Image')
    plt.subplot(1,3,2), plt.imshow(res), plt.title('Range of Blue, Green and RED')
    plt.subplot(1,3,3), plt.imshow(mask), plt.title('Mask')
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


def hist(picture):

    #img = cv.imread(picture)  # adquire a imagem do vídeo

    # juntar tudo na mesma imagem
    plt.figure(1)
    plt.subplot(221)
    plt.title('New Image')
    # tratamento da imagem original
    plt.imshow(picture)

    plt.subplot(222)
    plt.title('New Image Histogram')
    gray = cv.cvtColor(picture, cv.COLOR_BGR2GRAY)
    origin_hist = cv.calcHist([gray.ravel()], [0], None, [256], [5, 251])
    plt.plot(origin_hist)

    # tratamento da imagem para escala HSV
    plt.subplot(223)
    plt.title('HSV Image')
    hsv = cv.cvtColor(picture, cv.COLOR_BGR2HSV)  # img to HSV
    plt.imshow(hsv)

    plt.subplot(224)
    plt.title('HSV Image Histogram')
    hsv_hist = cv.calcHist([hsv.ravel()], [0], None, [256], [5, 251])
    plt.plot(hsv_hist)
    plt.show()



img = cv.imread("legoPictures/Legos9.jpg")
hist(img)
img = colorDetection(img)
img,contours=contour(img)
img=Measure.getMeasure(img, contours)


