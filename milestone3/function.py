import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from pyimagesearch.centroidtracker import CentroidTracker
import Measure


#def contour1(image):
#    #image = cv.imread(img)
#    imgray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
#    ret, thresh = cv.threshold(imgray, 0, 255, 0)
#    contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
#    cv.drawContours(image, contours, -1, (0,255,0), 6)
#
#
#    #img = image.imageResize(image)
#    image = cv.cvtColor(image, cv.COLOR_BGR2RGB)
#    cv.imshow('Display', image)
#    cv.waitKey(0)
#    cv.destroyAllWindows()
#    return image,contours


def contour(image, imgray):
    ret, thresh = cv.threshold(imgray, 0, 255, 0)
    contours, hierarchy = cv.findContours(thresh, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    #cv.drawContours(image, contours, -1, (0, 0, 0), 3)

    #cv.imshow('Contourns', image)
    #cv.waitKey(0)
    #cv.destroyAllWindows()
    return image, contours

def colorDetection(img):

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([112, 220, 50])
    upper_blue = np.array([120, 255, 255])
    lower_blue = np.array([112, 220, 50])
    upper_blue = np.array([120, 255, 255])

    # define range of green color in HSV
    lower_green = np.array([50, 100, 10])
    upper_green = np.array([105, 255, 255])
    lower_green = np.array([50, 100, 10])
    upper_green = np.array([105, 255, 255])

    # define range of red color in HSV
    lower_red = np.array([135, 155, 0])
    upper_red = np.array([179, 255, 255])
    lower_red = np.array([135, 155, 0])
    upper_red = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    mask3 = cv.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2 + mask3

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
    scale_percent = 40

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


    fgbg = cv.createBackgroundSubtractorMOG2()

    fgmask = fgbg.apply(background)


    fgmask = fgbg.apply(img)

    edges = cv.Canny(fgmask, 100, 200)

    #cv.imshow('edges',edges)
    #k = cv.waitKey(0) & 0xff

    return edges

def objectTracking(img):
    #creat rects array
    rects=[]
    #set a centroid tracker
    ct = CentroidTracker()

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)

    # define range of blue color in HSV
    lower_blue = np.array([112, 220, 50])
    upper_blue = np.array([120, 255, 255])

    # define range of green color in HSV
    lower_green = np.array([50, 100, 10])
    upper_green = np.array([105, 255, 255])

    # define range of red color in HSV
    lower_red = np.array([135, 155, 0])
    upper_red = np.array([179, 255, 255])

    # Threshold the HSV image to get only blue colors
    mask1 = cv.inRange(hsv, lower_blue, upper_blue)
    mask2 = cv.inRange(hsv, lower_green, upper_green)
    mask3 = cv.inRange(hsv, lower_red, upper_red)
    mask = mask1 + mask2 + mask3

    kernel = np.ones((2, 2), np.uint8)
    mask = cv.dilate(mask, kernel, iterations=1)
    mask = cv.erode(mask, kernel, iterations=1)

    res = cv.bitwise_and(img, img, mask=mask)
    framegray = cv.cvtColor(res, cv.COLOR_BGR2GRAY)
    framegray_b = cv.GaussianBlur(framegray, (3, 5), 0)
    edges = cv.Canny(framegray_b, 50, 150, apertureSize=3)

    red_mask = cv.dilate(mask3, kernel)
    res_red = cv.bitwise_and(img, img,
                             mask=red_mask)

    green_mask = cv.dilate(mask2, kernel)
    res_green = cv.bitwise_and(img, img,
                               mask=green_mask)

    blue_mask = cv.dilate(mask1, kernel)
    res_red = cv.bitwise_and(img, img,
                             mask=blue_mask)


    contours, hierarchy = cv.findContours(red_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv.boundingRect(contour)
            cv.putText(img, "Red", (x + w, y + h + 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1,
                       cv.LINE_AA)

            # Creating contour to track green color
    contours, hierarchy = cv.findContours(green_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)

    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv.boundingRect(contour)
            cv.putText(img, "Green", (x + w, y + h + 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1,
                       cv.LINE_AA)

    # Creating contour to track blue color
    contours, hierarchy = cv.findContours(blue_mask,
                                           cv.RETR_TREE,
                                           cv.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv.contourArea(contour)
        if (area > 300):
            x, y, w, h = cv.boundingRect(contour)

            cv.putText(img, "Blue", (x + w, y + h + 30), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1,
                       cv.LINE_AA)


    contours, hierarchy = cv.findContours(framegray_b, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
    for i in range(len(contours)):
        cnt = contours[i];

        if cv.contourArea(cnt) > 150 and hierarchy[0][i][3] == -1:
            x, y, w, h = cv.boundingRect(cnt)
            cv.rectangle(img, (x, y), (x + w, y + h), (255, 0, 155), 2)
            rects.append([x, y, x + w, y + h])
            unit_ref = 30
            ratio = [0, 0]
            ratio[0] = int(round(w / (unit_ref)))  # width
            ratio[1] = int(round(h / (unit_ref)))  # height

            cv.putText(img, str(ratio[0]) + "x" + str(ratio[1]), (x + w, y + h), cv.FONT_HERSHEY_SIMPLEX, 0.5,
                       (0, 0, 0), 1, cv.LINE_AA)

            objects = ct.update(rects)

            for box_id in objects:
                xi, yi, wi, hi, id = box_id

            cv.putText(img, "ID:" + str(id), (x + w, y + h + 13), cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1,
                       cv.LINE_AA)

    #cv.imshow('contours', img)
    #cv.waitKey(0) & 0xFF

    #cv.destroyAllWindows()
    return img