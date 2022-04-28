import cv2
import numpy as np

cnv = np.ones( (480,640,3),dtype=np.uint8() )
cap = cv2.VideoCapture ( 0 )

def findContour (frame_clr, out, cnv  ):
    cont, h = cv2.findContours (frame_clr,
                                 cv2.RETR_TREE,
                                 cv2.CHAIN_APPROX_SIMPLE)
    count = sorted (cont, key =cv2.contourArea, reverse = True)
    cv2.drawContours (out,cont, 0, (0,255,0), 2)
    cv2.drawContours (cnv,cont, 0, (0,255,0), -1)

    if len (cont):
        moments = cv2.moments (cont[0], 1)

        m00 = moments['m00']
        m01 = moments['m01']
        m10 = moments['m10']

        if  m00 > 100:
            x= int (m10/m00)
            y= int (m01/m00)
            cv2.circle( out, (x,y), 5, (0,255,255), -1)
            

while True:
    tr, frame = cap.read()
    frame_=cv2.blur (frame, (10,10) )
    frame_HSV = cv2.cvtColor(frame_, cv2.COLOR_BGR2HSV)

    clr_low = (15, 210, 110)
    clr_high = (40, 255, 255)

    frame_clr = cv2.inRange (frame_HSV, clr_low, clr_high)

    findContour (frame_clr, frame, cnv)

    cv2.imshow ('mask', frame_clr)
    cv2.imshow ('paint', cnv )

    cv2.imshow('main', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
