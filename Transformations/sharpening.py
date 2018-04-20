import cv2
import numpy as np

img=cv2.imread('mark.jpg')
cv2.imshow('original',img)
cv2.waitKey()

kernel_sharp=np.array([[-1,-1,-1],[-1,9,-1],[-1,-1,-1]])
sharpened=cv2.filter2D(img,-1,kernel_sharp)
cv2.imshow('Sharpened',sharpened)
cv2.waitKey()


cv2.destroyAllWindows()