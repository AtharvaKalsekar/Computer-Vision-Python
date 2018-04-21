import cv2
import numpy as np

img=cv2.imread('mark.jpg',0)

sobel_x=cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
sobel_y=cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
sobel_or=cv2.bitwise_or(sobel_x,sobel_y)
cv2.imshow('soble x',sobel_x)
cv2.waitKey()
cv2.imshow('soble y',sobel_y)
cv2.waitKey()
cv2.imshow('soble or',sobel_or)
cv2.waitKey()

laplacian=cv2.Laplacian(img,cv2.CV_64F)
cv2.imshow('Laplacian',laplacian)
cv2.waitKey()

canny=cv2.Canny(img,20,170)
cv2.imshow('canny',canny)
cv2.waitKey()

cv2.destroyAllWindows()