# Try to create the logo of OpenCV using drawing functions available in OpenCV.

import numpy as np
import cv2 as cv

# Create a black image
img = np.zeros((450,450,3), np.uint8)

cv.ellipse(img,(225,135),(100,100),90,30,330,(0,0,255),-1)
cv.ellipse(img,(225,135),(50,50),0,0,360,(0,0,0),-1)

cv.ellipse(img,(120,315),(100,100),0,0,300,(0,255,0),-1)
cv.ellipse(img,(120,315),(50,50),0,0,360,(0,0,0),-1)

cv.ellipse(img,(330,315),(100,100),270,35,325,(255,0,0),-1)
cv.ellipse(img,(330,315),(50,50),0,0,360,(0,0,0),-1)

# Display the image
cv.imshow("Display window", img)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("logo.jpg", img)