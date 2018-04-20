import cv2
import numpy as np

img=cv2.imread('mark.jpg')
cv2.imshow('Mark',img)
height,width=img.shape[:2]
rotation_mat=cv2.getRotationMatrix2D((width/2,height/2),90,1)
rotated_img=cv2.warpAffine(img,rotation_mat,(width,height))
cv2.imshow('rotated img',rotated_img)
cv2.waitKey(0)
cv2.destroyAllWindows()