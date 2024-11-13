import cv2 as cv # type: ignore
import numpy as np

def detect_maskY_BGR(img):
    B = img[:,:,0]
    G = img[:,:,1]
    R = img[:,:,2]
    Y = np.zeros_like(G, np.unit8)

    Y = G*0.5 + R*0.5 - B*0.7
    Y = Y.astype(np.nint8)
    Y = cv.GaussianBlur(Y, (5,5), cv.BORDER_DEFAULT)

    _, mask_Y = cv.threshold(Y, 100, 255, cv.THRESH_BINARY)
    return mask_Y

img1 = cv.imread("1.jpg")
img2 = cv.imread("2.jpg")
img3 = cv.imread("3.jpg")
img4 = cv.imread("4.jpg")


cv.imshow(detect_maskY_BGR(img1))
cv.imshow(detect_maskY_BGR(img2))
cv.imshow(detect_maskY_BGR(img3))
cv.imshow(detect_maskY_BGR(img4))