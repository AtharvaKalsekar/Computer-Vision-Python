import cv2
import numpy as np


img=cv2.imread('scaleofgray.png',0)
cv2.imshow('original',img)
cv2.waitKey()

ret,thresh1=cv2.threshold(img,127,255,cv2.THRESH_BINARY)
cv2.imshow('thresh 1',thresh1)
cv2.waitKey()

ret,thresh2=cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
cv2.imshow('thresh 2',thresh2)
cv2.waitKey()

ret,thresh3=cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
cv2.imshow('thresh 3',thresh3)
cv2.waitKey()

ret,thresh4=cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
cv2.imshow('thresh 4',thresh4)
cv2.waitKey()

ret,thresh5=cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)
cv2.imshow('thresh 5',thresh5)
cv2.waitKey()

textimg=cv2.imread('text.jpeg',0)
blur=cv2.GaussianBlur(textimg,(5,5),0)
thresh6=cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,3,5)
cv2.imshow('thresh 6',thresh6)
cv2.waitKey()

ret,thresh7=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('thresh 7',thresh7)
cv2.waitKey()

cv2.destroyAllWindows()