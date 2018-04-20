import cv2
import numpy as np

img = cv2.imread('mark.jpg')
cv2.imshow('original',img)
cv2.waitKey()
img_small=cv2.pyrDown(img)
cv2.imshow('Pyr down',img_small)
cv2.waitKey()
img_large=cv2.pyrUp(img)
cv2.imshow('Pyr up',img_large)
cv2.waitKey()
cv2.destroyAllWindows()