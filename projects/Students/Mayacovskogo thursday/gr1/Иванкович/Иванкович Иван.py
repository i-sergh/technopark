import cv2

cap = cv2.VideoCapture( 'in.mp4' )

while True:
    tr, frame = cap.read()
    if not tr:
        cap = cv2.VideoCapture( 'in.mp4' )
        tr, frame = cap.read()
        
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )

    clr_low = (0, 0, 110)
    clr_high = (180, 40, 255)

    frame_clr = cv2.inRange (frame_HSV, clr_low, clr_high )
    
    
    cv2.imshow( 'mask', frame_clr )
    cv2.imshow( 'main', frame )

    if cv2.waitKey(1) == ord('l'):
        break

cv2.destroyAllWindows()

cap.release()
    
