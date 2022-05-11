import cv2
import numpy as np
cap = cv2.VideoCapture (0)
last_frame = np.zeros((480,640), dtype=np.uint8())
while True:
    
    rt, frame = cap.read()
    frame_ = cv2.blur(frame, (10, 10) )
    frame_HSV = cv2.cvtColor(frame_,
                             cv2.COLOR_BGR2HSV)

    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange(frame_HSV, clr_low ,clr_high)
    
    cv2.imshow('mask' , frame_clr ) 
    cv2.imshow('dvij' , frame_clr -  last_frame) 
    cv2.imshow('main' , frame)
    last_frame = frame_clr
    frame_clr = frame_clr -  last_frame
    
    cont = cv2.findContours(frame_clr , cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)[0]
    
    if  np.count_nonzero(frame_clr -  last_frame) >6000:
        print("YOU'RE MOVING!", np.count_nonzero(frame_clr -  last_frame))
    else:
        print("where are you?!")
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
