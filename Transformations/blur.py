import cv2
import numpy as np

img=cv2.imread('mark.jpg')
cv2.imshow('Orig',img)
cv2.waitKey()
kernel_7=np.ones((7,7),np.uint8)/49
blur_manual=cv2.filter2D(img,-1,kernel_7)
cv2.imshow('filter2d',blur_manual)
cv2.waitKey()
blur_gaussian=cv2.GaussianBlur(img,(7,7),0)
cv2.imshow('Gaussian blur',blur_gaussian)
cv2.waitKey()
blur_median=cv2.medianBlur(img,5)
cv2.imshow('Median blur',blur_median)
cv2.waitKey()
blur_bilateral=cv2.bilateralFilter(img,9,75,75)
cv2.imshow('Bilateral filter',blur_bilateral)
cv2.waitKey()
blur_nlm=cv2.fastNlMeansDenoisingColored(img,None,6,6,7,21)
cv2.imshow('Blur nlm',blur_nlm)
cv2.waitKey()
cv2.destroyAllWindows()