import cv2
import numpy as np
 
cap = cv2.VideoCapture(0)
i=0

if (cap.isOpened()== False): 
  print("Error opening video stream or file")
 
while(cap.isOpened()):
  ret, frame = cap.read()
  if ret == True:
    cv2.imshow('Frame',frame)
    # Press Q on keyboard to  exit
    if cv2.waitKey(25) & 0xFF == ord('q'):
      break

    if cv2.waitKey(27) & 0xFF == ord('a'):
        name="capture"+str(i)+".jpg"
        cv2.imwrite(name,frame)
        print("capture"+str(i))
        i+=1
  else: 
    break
cap.release()
cv2.destroyAllWindows()
