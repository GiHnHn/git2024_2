import  cv2 as cv # type: ignore
import numpy as np

cap = cv.VideoCapture(0)

if not cap.isOpened():
    print("Cannot open camer")
    exit()

while True:

    ret, frame =cap.read()

    if not ret:
        print("can't receive frame (stream end?)")
        break

    #gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    cv.imshow('frame', frame)
    if cv.waitKey(1)==ord('q'):
        break

cap.release()
cv.destroyAllWindows()