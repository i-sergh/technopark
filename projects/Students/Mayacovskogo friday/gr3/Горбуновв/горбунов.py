import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def findDot (color_mask, cnv):
    
    moments = cv2.moments(color_mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(cnv, (x, y), 10, (0,0,255), -1)

def drawFirstAndSecondContour(color_mask, cnv):
    contours, hierarchy = cv2.findContours( color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    contours = sorted(contours, key=cv2.contourArea, reverse = True)
    
    try:
        if cv2.contourArea(contours[0]) > 100:
            cv2.drawContours( cnv, contours, contourIdx=0, color=(0,255,0), thickness=1 )
            cv2.drawContours( cnv, contours, contourIdx=1, color=(255,255,0), thickness=1 )
    except:
        pass

img_do=cv2.imread('akne3.jpg')
img_posle=cv2.imread('out.png')
while True:
    ret, frame = cap.read()
    #frame_HSV = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) 
    # красный 
    #red_low = (0,140,160)
    #red_high = (15,255,255)

    
    #frame_reds = cv2.inRange(frame_HSV, red_low, red_high)
    

    cv2.imshow('original', img_do )
    cv2.imshow('l', img_posle )
    img_res = img_do - img_posle
    cv2.imshow('nal', img_res )
    
    #cv2.imshow('original', frame )
    #cv2.imshow('red', frame_reds )
    if cv2.waitKey(1) == 27:
        break



cap.release()
cv2.destroyAllWindows()
