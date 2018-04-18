import cv2
from matplotlib import pyplot as plt
img=cv2.imread('mark.jpg')
cv2.imshow('image',img)
cv2.waitKey()
color=('b','g','r')
for i,col in enumerate(color) :
    hist=cv2.calcHist([img],[i],None,[256],[0,256])
    plt.plot(hist,color=col)
    plt.xlim([0,256])
plt.show()
cv2.destroyAllWindows()