import cv2
import numpy as np


def callback(x):
    pass

def morphing(input_image):
    gray=cv2.cvtColor(input_image,cv2.COLOR_BGR2GRAY)
    gray = cv2.bilateralFilter(gray, 11, 17, 17)
    _,thresh=cv2.threshold(gray,50,255,cv2.THRESH_BINARY)
    kernel = np.ones((7,7),np.uint8)
    threshErode=cv2.erode(thresh,kernel,iterations=2)
    threshDilate=cv2.dilate(threshErode,kernel,iterations=2)
    return threshDilate

def draw(frame,x,y,text):
    cv2.circle(frame, (x, y), 5, (0,255, 0), -1)
    cv2.circle(frame, (x, y), 50, (0, 255, 0), 2, lineType=8)
    cv2.putText(frame, text, (x+60, y+60), cv2.FONT_HERSHEY_COMPLEX, 1, (0, 255, 0), 1, cv2.LINE_AA)

def contoursAndArea(input_image,color_image):
    edged = cv2.Canny(input_image, 30, 200)
    _,cnts,_ = cv2.findContours(edged.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:10]


    for c in cnts:
        area2 = cv2.contourArea(c)
        M = cv2.moments(c)
        if(M["m00"] > 0):
            cX = int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            return cX,cY
    return 0,0


cap = cv2.VideoCapture(1)
cv2.namedWindow('image')
cv2.resizeWindow('image', 640,480)

ilowH = 0
ihighH = 179

ilowS = 0
ihighS = 255
ilowV = 0
ihighV = 255

# create trackbars for color change
cv2.createTrackbar('lowH','image',ilowH,179,callback)
cv2.createTrackbar('highH','image',ihighH,179,callback)

cv2.createTrackbar('lowS','image',ilowS,255,callback)
cv2.createTrackbar('highS','image',ihighS,255,callback)

cv2.createTrackbar('lowV','image',ilowV,255,callback)
cv2.createTrackbar('highV','image',ihighV,255,callback)

while(cap.isOpened()):

    ret, frame = cap.read()
    ilowH = cv2.getTrackbarPos('lowH', 'image')
    ihighH = cv2.getTrackbarPos('highH', 'image')
    ilowS = cv2.getTrackbarPos('lowS', 'image')
    ihighS = cv2.getTrackbarPos('highS', 'image')
    ilowV = cv2.getTrackbarPos('lowV', 'image')
    ihighV = cv2.getTrackbarPos('highV', 'image')

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    '''
    lower_hsv = np.array([ilowH, ilowS, ilowV])
    higher_hsv = np.array([ihighH, ihighS, ihighV])
    '''
    #Blue
    lower_hsv_b = np.array([100, 68, 76])
    higher_hsv_b = np.array([110, 214, 185])
    #Red
    lower_hsv_r = np.array([151, 96, 0])
    higher_hsv_r = np.array([179, 255, 255])

    #mask = cv2.inRange(hsv, lower_hsv, higher_hsv)
    mask_b = cv2.inRange(hsv, lower_hsv_b, higher_hsv_b)
    mask_r = cv2.inRange(hsv, lower_hsv_r, higher_hsv_r)

    #frame1 = cv2.bitwise_and(frame, frame, mask=mask)
    frame1_b = cv2.bitwise_and(frame, frame, mask=mask_b)
    frame1_r = cv2.bitwise_and(frame, frame, mask=mask_r)
    
    #filteredMorph=morphing(frame1)
    filteredMorph_b=morphing(frame1_b)
    filteredMorph_r=morphing(frame1_r)
    '''
    cv2.imshow('Filterd Morph',filteredMorph)
    '''
    #x,y =contoursAndArea(filteredMorph,frame)
    x_b,y_b =contoursAndArea(filteredMorph_b,frame)
    x_r,y_r =contoursAndArea(filteredMorph_r,frame)
    
    '''
    if(x!= 0) :
        draw(frame,x,y)
    '''
    if(x_b!= 0) :
        draw(frame,x_b,y_b,'Bottle')

    if(x_r!= 0) :
        draw(frame,x_r,y_r,'Box')
    
    #cv2.imshow('Filtered image',frame1)
    cv2.imshow('Eyes', frame)
    k = cv2.waitKey(10) & 0xFF
    if k == 13 or k == 27:
        break

cap.release()
cv2.destroyAllWindows()