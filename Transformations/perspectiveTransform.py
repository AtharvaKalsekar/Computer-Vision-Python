import cv2
import numpy as np

pts_A = []
i = 0

def onClick(action,x,y,flags,userdata):
    global pts_A,i
    if action==cv2.EVENT_LBUTTONDOWN :
        if i<4 :
            pts_A.append((x,y))
            print(pts_A[i])
            i=i+1
        if i>=4 :
            i=0

def transform(img):
    global pts_A
    pts_B=np.float32([[0,0],[500,0],[500,500],[0,500]])
    pts_A=np.float32(pts_A)
    M=cv2.getPerspectiveTransform(pts_A,pts_B)
    warped=cv2.warpPerspective(img,M,(500,500))
    cv2.imshow('Warped',warped)
    cv2.waitKey()

img=cv2.imread('contours.jpg')
cv2.namedWindow('Original')
cv2.setMouseCallback('Original',onClick)
cv2.imshow('Original',img)
cv2.waitKey()
transform(img)

#pts_A=np.float32([[320,25],[700,215],[85,610],[530,780]])
'''pts_A=np.zeros((4,2))
y=1
for i in range(len(pts_A)):
    pts_A[i]=onClick()
    print(pts_A[i])
#print(pts_A[1])
#pts_B=np.float32([[0,0],[420,0],[0,594],[420,594]])
#M=cv2.getPerspectiveTransform(pts_A,pts_B)
#warped=cv2.warpPerspective(img,M,(420,594))
#cv2.imshow('Original',img)
#cv2.waitKey()
#cv2.imshow('Warped',warped)
cv2.waitKey()'''
cv2.destroyAllWindows()