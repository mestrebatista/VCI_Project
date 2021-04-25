# Image resizing program
import cv2 as cv
import sys

def imageResize(image):

    # Percent of original size
    scale_percent = 20

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


img = cv.imread(cv.samples.findFile("groundtruth-rot0-2.png"))
if img is None:
    sys.exit("Could not read the image.")

img = imageResize(img)

cv.imshow('image',img)
k = cv.waitKey(0) & 0xFF

