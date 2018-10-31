from panorama import Stitcher
import argparse
import imutils
import cv2

cap = cv2.VideoCapture(1)
cv2.namedWindow('Eyes')
cv2.resizeWindow('Eyes', 640,480)
images=[]
print('Click first Image')
while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('Eyes', frame)
    k = cv2.waitKey(10) & 0xFF
    if(k==ord('a')):
        print('Image Saved')
        images.append(frame)
        print('Click Next Image')
    if(len(images)==2):
        break
    if k == 13 or k == 27:
        break
'''
imageA = cv2.imread("1.jpg")
imageB = cv2.imread("2.jpg")
'''
cap.release()
cv2.destroyAllWindows()

imageA = imutils.resize(images[0], width=400)
imageB = imutils.resize(images[1], width=400)
#imageC = imutils.resize(images[2], width=400)

stitcher = Stitcher()
(result, vis) = stitcher.stitch([imageA, imageB], showMatches=True)
cv2.imshow("Image A", imageA)
cv2.imshow("Image B", imageB)
cv2.imshow("Keypoint Matches 1", vis)
'''
(result, vis) = stitcher.stitch([result, imageC], showMatches=True)

cv2.imshow("Image C", imageC)
cv2.imshow("Keypoint Matches 2", vis)
'''
cv2.imshow("Result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()