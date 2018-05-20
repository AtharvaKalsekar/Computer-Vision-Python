import cv2
import numpy as np

src=np.zeros((500,700),dtype=np.float32)
cv2.rectangle(src,(10,10),(300,300),(255,255,255),-1)
cv2.rectangle(src,(50,50),(250,250),(0,0,0),-1)
cv2.rectangle(src,(400,10),(600,400),(255,255,255),-1)
cv2.imshow('rects',src)
cv2.waitKey()
cv2.imwrite('shapes.jpg',src)
cv2.destroyAllWindows()