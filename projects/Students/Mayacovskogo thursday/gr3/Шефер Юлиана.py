import cv2

cap = cv2.VideoCapture ( 0 )
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)

    clr_low = (5, 57, 20)
    clr_high = (40, 255, 180)

    frame_clr = cv2.inRange ( frame_HSV, clr_low, clr_high )

    cv2.imshow('mask', frame_clr )
    cv2.imshow('main', frame )
    
    if cv2.waitKey(1) == ord ('q') :
        break
    
cap.release()
cv2.destroyAllWindows()

