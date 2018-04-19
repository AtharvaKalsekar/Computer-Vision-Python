import cv2
import numpy as np

img=cv2.imread('mark.jpg')
width,height=img.shape[:2]
q_width,q_height=width/4,height/4
T= np.float32([[0,1,q_width],[1,0,q_height]])
img_trans=cv2.warpAffine(img,T,(width,height))
cv2.imshow('Translation',img_trans)
cv2.waitKey(0)
cv2.destroyAllWindows()