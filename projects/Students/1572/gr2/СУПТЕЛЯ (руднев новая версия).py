import cv2
import numpy as np


cap = cv2.VideoCapture( 0 )

cnv =  np.ones( (480, 640, 3), dtype=np.uint8() ) 


def findContour ( clr_mask, out ):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont, key=cv2.contourArea, reverse=True )
    cv2.drawContours( out, cont, 0, (0,255,0), 2 )
    cv2.drawContours( cnv, cont, 0, (0,255,0), -1 )

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame,
                              cv2.COLOR_RGB2HSV )
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)
    
    frame_clr = cv2.inRange( frame_HSV,
                             clr_low,
                             clr_high)
    findContour( frame_clr, frame )
    cv2.imshow('mask', frame_clr )
    cv2.imshow('paint', cnv )
    
    cv2.imshow( 'main', frame )

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
