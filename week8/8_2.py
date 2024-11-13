import cv2 as cv # type: ignore

events = [i for i in dir(cv) if 'EVENT' in i]
print(events)