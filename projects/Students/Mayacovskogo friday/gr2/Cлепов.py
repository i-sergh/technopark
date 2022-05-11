import cv2
from random import randint
import numpy as np
cap = cv2.VideoCapture( 0 )

def findContour( clr_mask, out ):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    #cv2.drawContours( out, cont, 0, (0,255,0), 2)
    
    try:
        moments = cv2.moments(cont[0], 1)

        m00 = moments['m00']
        clr_mask = np.zeros((480, 640), dtype=np.uint8() )
        cv2.drawContours(clr_mask, cont, 0, (255,255,255), -1)
        return clr_mask
    except:
        return None

def freckles(mask, out ):
    for i in range(100):
        x = randint(0,639)
        y = randint(0, 479)
        if mask[y, x] == 255:
            cv2.circle(out, (x, y), randint(1, 5), (randint(0,255), randint(0,255), randint(0,255)), -1)        
    
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    clr_low = (0, 70, 110)
    clr_high = (30, 150, 255)

    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    cont = findContour(frame_clr,frame)

    if not type(cont) == "<class 'NoneType'>":
        freckles(cont, frame )
    
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey(1) == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
