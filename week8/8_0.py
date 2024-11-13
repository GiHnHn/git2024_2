import sys
import cv2 as cv # type: ignore

img = cv.imread("img.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display window", img)
k = cv.waitKey(0)

if k == ord("s"):
    cv.imwrite("img.png", img)