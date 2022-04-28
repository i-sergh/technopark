import cv2

cap=cv2.VideoCapture(0)

def findContour( clr_mask, out):
    cont, h = cv2.findContours( clr_mask,
                                 cv2.RETR_TREE,
                                 cv2.CHAIN_APPROX_SIMPLE )
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,255,0),2 )
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    clr_low = (0,210, 110)
    clr_high = (15, 255, 255)

    clr_low2 = (0,128,0)
    clr_high2 = (0,128,0)

    clr_low3 = (0,30,50)
    clr_high3 = (40,255,70)

    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )
    
    

    frame_clr2 = cv2.inRange( frame_HSV, clr_low2, clr_high2 )

    frame_clr3 = cv2.inRange( frame_HSV, clr_low3, clr_high3 )

    findContour(frame_clr3,frame)

    cv2.imshow("mask", frame_clr3)
    

    cv2.imshow( "main", frame )

    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
