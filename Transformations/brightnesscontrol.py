import cv2
import numpy as np

img=cv2.imread('mark.jpg')
M=np.ones(img.shape,dtype="uint8")*75
added=cv2.add(img,M)
cv2.imshow('brightness ++',added)
cv2.waitKey()
subtracted=cv2.subtract(img,M)
cv2.imshow('brightness --',subtracted)
cv2.waitKey()
cv2.destroyAllWindows()