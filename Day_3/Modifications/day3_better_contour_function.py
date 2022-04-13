import cv2

cap = cv2.VideoCapture( 0 )

def findContour ( clr_mask, out, color=(255,255,255) ):

    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE )
    cont = sorted( cont, key=cv2.contourArea, reverse=True )
    
    cv2.drawContours( out, cont, 0, color , 2 )
    cv2.drawContours( clr_mask, cont, 0, (0,0,0) , -1 ) 
    
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor ( frame, cv2.COLOR_BGR2HSV )
               # H   S    V
    clr_low =  ( 0, 210, 110 )
    clr_high = (15, 255, 255 )

    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )

    cv2.imshow('mask before change', frame_clr )

    findContour( frame_clr, frame )
    
    findContour( frame_clr, frame, (0,255,0) )
    
    cv2.imshow('mask after change', frame_clr )

    cv2.imshow('main', frame )

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
