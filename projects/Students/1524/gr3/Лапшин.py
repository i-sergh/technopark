import cv2

cap = cv2.VideoCapture( 0 )

while True:
    tr, frame = cap.read()
    
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    
    clr_low = (0, 210, 110)
    
    clr_high = (15, 255, 255)
    #clr_low = (0, 0, 110)
    #clr_high = (180, 70, 255)
    
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )

    frame[frame_clr==255] = (0,255,0) 
    
    cv2.imshow('mask', frame_clr )
    
    cv2.imshow('mask n', frame )
    
    if cv2.waitKey(1) == ord('q'):
        
        break
cap.release()

cv2.destroyAllWindows()
