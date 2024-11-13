import cv2 as cv
import numpy as np

def selectyellowline(image):
    hsv =cv.cvtColor(image, cv.COLOR_BGR2HSV)
    minyellow =np.array([26, 55, 190])
    maxyellow =np.array([40, 255, 255])
    mask =cv.inRange(hsv, minyellow, maxyellow)

    result =cv.bitwise_and(image, image, mask=mask)
    return result

img1 = cv.imread('1.jpg') 
img2 = cv.imread('2.jpg') 
img3 = cv.imread('3.jpg') 
img4 = cv.imread('4.jpg') 
img1_blur = cv.GaussianBlur(img1,(5,5),0)
img2_blur = cv.GaussianBlur(img2,(5,5),0)
img3_blur = cv.GaussianBlur(img3,(5,5),0)
img4_blur = cv.GaussianBlur(img4,(5,5),0)
res1=selectyellowline(img1_blur)
res2=selectyellowline(img2_blur)
res3=selectyellowline(img3_blur)
res4=selectyellowline(img4_blur)

cv.imshow('img1',res1)
cv.imshow('img2',res2)
cv.imshow('img3',res3)
cv.imshow('img4',res4)
cv.waitKey(0)
cv.destroyAllWindows() 