import cv2
import numpy as np
cap = cv2.VideoCapture( 0 )

while True:
    tr, frame = cap.read()
    cv2.imshow('main', frame )
    frame = cv2.flip(frame, 2)
    frame_HSV = cv2.cvtColor( frame,
                              cv2.COLOR_BGR2HSV )
    #clr_low = (0, 210, 
    

    cv2.imshow('mirror', frame )

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.realease()
    
