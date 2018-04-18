import cv2
img=cv2.imread('/home/atharva/Downloads/OPENCV COURSE/learnopencv/day-2-more-operations/mark.jpg')
cv2.imshow('mark',img)
print (img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()