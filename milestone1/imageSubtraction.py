import numpy as np
import cv2

def get_difference(image_path_1, image_path_2, cnt):
    image1 = cv2.imread(image_path_1)
    image2 = cv2.imread(image_path_2)
    difference = cv2.subtract(image1, image2)
    Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(Conv_hsv_Gray, 0, 255,cv2.THRESH_BINARY_INV |cv2.THRESH_OTSU)
    #difference[mask != 255] = [0, 0, 255]
    # image1[mask != 255] = [0, 0, 255]
    # image2[mask != 255] = [0, 0, 255]
    #cv2.imwrite('difference_img/diff_image_' + str(cnt) + '.png', image1)
    cv2.imwrite(str(cnt) + '.png', mask)


get_difference('fundo.jpg','legoImage.png','result')