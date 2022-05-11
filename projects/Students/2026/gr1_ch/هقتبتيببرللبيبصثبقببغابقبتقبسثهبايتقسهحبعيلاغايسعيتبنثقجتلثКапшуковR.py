import cv2

cap = cv2.VideoCapture(0)

def findContour( clr_mask, out ):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    cv2.drawContours( out, cont, 0, (199,25,79), 2)

    if len(cont) :
        moments = cv2.moments(cont[0], 1)
        m00 = moments['m00']
        m01 = moments['m01']
        m10 = moments['m10']
        if m00 >100:
            x = int(m10 / m00)
            y = int(m01 / m00)
            cv2.circle( out, (x,y), 5, (0,255,255), -1)
while True:

    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor (frame, cv2.COLOR_BGR2HSV)
    clr_low = (0, 25, 110)
    clr_high = (15, 255, 255)
    frame_clr = cv2.inRange (frame_HSV, clr_low, clr_high)

    findContour( frame_clr, frame )
    
    cv2. imshow( 'mask', frame_clr )
    cv2.imshow( 'main', frame)

    if cv2.waitKey(1) == 27:
        break

cv2.destroyAllWindows()
cap.release()
