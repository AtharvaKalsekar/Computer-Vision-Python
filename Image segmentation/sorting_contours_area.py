import cv2
import numpy as np

img=cv2.imread('shapes.jpg')
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
edge=cv2.Canny(gray,50,200)
