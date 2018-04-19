import cv2
img=cv2.imread('/home/atharva/Downloads/OPENCV COURSE/learnopencv/day-2-more-operations/mark.jpg')
cv2.imshow('orig',img)
cv2.waitKey()
gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imshow('grey',gray)
cv2.waitKey()
cv2.destroyAllWindows()