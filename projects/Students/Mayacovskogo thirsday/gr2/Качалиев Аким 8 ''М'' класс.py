import cv2

cap = cv2.VideoCapture( 0 )

while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)

    cir_low = (0,210, 110)
    cir_high = (15, 255, 255)

    frame_cir = cv2.inRange( frame_HSV, cir_low, cir_high )

    

    cv2.imshow( 'main', frame_cir )
    cv2.imshow('main', frame)
    

    if cv2.waitKey(1) == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
