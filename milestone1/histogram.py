import cv2 as cv
from matplotlib import pyplot as plt

def hist(picture):

    img = cv.imread(picture)  # adquire a imagem do vídeo

    # juntar tudo na mesma imagem
    plt.figure(1)
    plt.subplot(221)
    plt.title('New Image')
    # tratamento da imagem original
    plt.imshow(img)

    plt.subplot(222)
    plt.title('New Image Histogram')
    origin_hist = cv.calcHist([img], [0], None, [256], [1, 255])
    plt.plot(origin_hist)

    # tratamento da imagem para escala HSV
    plt.subplot(223)
    plt.title('HSV Image')
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # img to HSV
    plt.imshow(hsv)

    plt.subplot(224)
    plt.title('HSV Image Histogram')
    hsv_hist = cv.calcHist([hsv.ravel()], [0], None, [256], [1, 255])
    plt.plot(hsv_hist)
    plt.show()





