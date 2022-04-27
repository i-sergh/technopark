import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def findCenter (clr_mask, cnv):
    
    moments = cv2.moments(clr_mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(cnv, (x, y), 10, (0,0,255), -1)

def findContour(color_mask, out ):
    cont, h= cv2.findContours( color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    cont = sorted(cont, key=cv2.contourArea, reverse = True)
    
    try:
        cv2.drawContours( out, cont, contourIdx=0, color=(0,255,0), thickness=1 )
        
        findCenter(cont[0], out)
    except:
        pass

while True:
    ret, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) 
    # красный 
    clr_low = (0,150,110)
    clr_high = (15,255,255)

    
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)


    findCenter(frame_clr, frame)
    findContour(frame_clr, frame)

    cv2.imshow('original', frame )
    cv2.imshow('red', frame_clr )
    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
