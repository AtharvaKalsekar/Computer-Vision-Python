import cv2
import numpy as np

img=cv2.imread('mark.jpg')
cv2.imshow('Mark',img)
height,width=img.shape[:2]
q_width,q_height=width/4,height/4
T = np.float32([[1,0,q_width],[0,1,q_height]])
print (T)
img_trans=cv2.warpAffine(img,T,(width,height))
cv2.imshow('Translation',img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()