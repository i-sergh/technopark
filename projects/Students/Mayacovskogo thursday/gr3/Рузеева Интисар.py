import cv2
import numpy as np
cap = cv2.VideoCapture( 0 )

while True:
    tr, frame = cap.read()
    frame_ = cv2.blur( frame, (5,5) ) 
    frame_HSV = cv2.cvtColor( frame_, cv2.COLOR_BGR2HSV )

    clr_low = (0,0,110)
    clr_high = (180,70,255)

    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high )

    cv2.imshow('mask', frame_clr )
    cv2.imshow('main', frame )
    
    print(np.count_nonzero(frame_clr))

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

