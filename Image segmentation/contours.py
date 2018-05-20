import cv2
import numpy as np

#src=cv2.imread('shapes.jpg')
src=cv2.imread('/home/atharva/Downloads/OPENCV COURSE/counting glasses project/a1-t3.jpg')
if src is not None :
    cv2.imshow('rects',src)
else :
    print('Image not loaded')
    exit()
'''
src=cv2.bitwise_and(src,src)
'''
gray=cv2.cvtColor(src,cv2.COLOR_BGR2GRAY)

edge=cv2.Canny(gray,50,200)
cv2.imshow('canny edges 1',edge)
_,contours,hierarchy= cv2.findContours(edge,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
print('Length of contours '+str(len(contours))+"\n")
print(contours)
cv2.imshow('canny edges 2',edge)
cv2.drawContours(src,contours,-1,(255,0,0),1)
cv2.imshow('contours',src)

cv2.waitKey()

#cv2.imwrite('shapes.jpg',src)
cv2.destroyAllWindows()