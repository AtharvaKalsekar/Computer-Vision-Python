import cv2
import numpy as np

img = cv2.imread('mark.jpg')

zoom_out=cv2.resize(img,None,fx=0.5,fy=0.5,interpolation=cv2.INTER_AREA)
cv2.imshow('Zoom out',zoom_out)
cv2.waitKey()

zoom_in=cv2.resize(img,None,fx=1.2,fy=1.2,interpolation=cv2.INTER_LINEAR)
cv2.imshow('Zoom in',zoom_in)
cv2.waitKey()

cv2.destroyAllWindows()