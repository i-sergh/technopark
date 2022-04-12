import cv2

cap = cv2.VideoCapture( 0 )

while True:
    ret, frame = cap.read()

    cv2.imshow( 'main before change', frame )

    frame[ 200:, :200, 0 ] = 0
    frame[ 100:, :100, 2 ] = 0
    
    frame[ 100:350:4 , 300:550, 0:2 ] = 0
    
    cv2.imshow( 'main after change', frame )
    if cv2.waitKey( 1 ) == ord( 'q' ):
        break

cap.release()
cv2.destroyAllWindows()
