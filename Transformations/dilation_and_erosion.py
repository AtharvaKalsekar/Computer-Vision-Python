import cv2
import numpy as np

cir=np.zeros((500,500),np.uint8)
cir_=cv2.circle(cir,(int(cir.shape[0]/2),int(cir.shape[1]/2)),50,(255,255,255),3)
cv2.imshow('circle',cir_)
cv2.waitKey()

kernel=np.ones((5,5),np.uint8)

erosion=cv2.erode(cir_,kernel,iterations=1)
cv2.imshow('Eroded',erosion)
cv2.waitKey()

dilation=cv2.dilate(cir_,kernel,iterations=1)
cv2.imshow('Dilated',dilation)
cv2.waitKey()

opening=cv2.morphologyEx(cir_,cv2.MORPH_OPEN,kernel)
cv2.imshow('Opening',opening)
cv2.waitKey()

closing=cv2.morphologyEx(cir_,cv2.MORPH_CLOSE,kernel)
cv2.imshow('Closing',closing)
cv2.waitKey()


cv2.destroyAllWindows()