import cv2
import numpy as np

square=np.zeros((300,300),np.uint8)
cv2.rectangle(square,(50,50),(250,250),255,-1)
cv2.imshow('square',square)

ellipse=np.zeros((300,300),np.uint8)
cv2.ellipse(ellipse,(150,150),(150,150),30,0,180,255,-1)
cv2.imshow('ellipse',ellipse)
cv2.waitKey()

And=cv2.bitwise_and(square,ellipse)
cv2.imshow('and',And)
cv2.waitKey()

Or=cv2.bitwise_or(square,ellipse)
cv2.imshow('or',Or)
cv2.waitKey()

Xor=cv2.bitwise_xor(square,ellipse)
cv2.imshow('xor',Xor)
cv2.waitKey()

Not=cv2.bitwise_not(square)
cv2.imshow('not',Not)
cv2.waitKey()

cv2.destroyAllWindows()