import cv2
import numpy as np

cnv = np.zeros (  (480,640,3), dtype=np.uint8() )

cap = cv2.VideoCapture( 0 )


def findCenter(frame_mask, out, txt = ''):
    moments = cv2.moments(frame_mask, 1)
    m00 = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']

    if m00>100:
        x = int(m10/m00)
        y = int(m01/m00)
        cv2.circle(out, (x,y), 5, (255,0,255), -1)
        cv2.putText(out, txt, (x-100,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (255,0,255), 2)


def findContour( frame_mask, out, cnv):
    global fcount
    cont, h = cv2.findContours( frame_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key = cv2.contourArea, reverse = True)
    cv2.drawContours( out, cont, 0, (0,255,0), 2)
    
    if len(cont):
        if cv2.contourArea(cont[0])>10000:
            if fcount> 20:
                
                cv2.drawContours( cnv, cont, 0, (0,255,255), -1)
                fcount = 0
            findCenter( cont[0], out, '*PUNCH*')

global fcount
fcount = 0
while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)

    clr_low = (15, 150, 100)
    clr_high = (40, 255, 255)
    
    
    
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    #frame = frame +cnv

    frame [frame > cnv] = frame [frame > cnv] + cnv[frame > cnv]  
    frame [frame < cnv] =  cnv[frame < cnv]
    findContour( frame_clr, frame, cnv)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    cv2.imshow('cnv', cnv)
    if cv2.waitKey(1) == ord('q'):
        break
    fcount+=1
    cnv[cnv > 0] -= 1
cap.release()
cv2.destroyAllWindows()

    
