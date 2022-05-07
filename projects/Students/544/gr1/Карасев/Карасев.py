import cv2
#cap = cv2.VideoCapture( 0 )

vid = cv2.VideoCapture('cyclone.mp4')

def findContour( clr_mask, out ):
    cont, h = cv2.findContours(clr_mask, cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont, key=cv2.contourArea, reverse = True )
    cv2.drawContours( out, cont, 0, (0,255,0), 2 )

    if len(cont) > 0:
        moments = cv2.moments( cont[0], 1 )

        m00 = moments['m00']
        m01 = moments['m01']
        m10 = moments['m10']

        if m00 > 100:
            x = int( m10 / m00 )
            y = int( m01 / m00 )

            cv2.circle( out, (x,y), 5, (0, 150,255), -1)
            cv2.putText(out, str(m00), (x,y),
                        cv2.FONT_HERSHEY_TRIPLEX, 1, (0, 150,255) , 2 )
            

while True:
   
    rt, frameV = vid.read()
    if not rt:
        vid = cv2.VideoCapture('cyclone.mp4')
        rt, frameV = vid.read()
    frame_HSV = cv2.cvtColor(frameV,cv2.COLOR_BGR2HSV)
    
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)

    clr_low = (0, 0, 110)
    clr_high = (180, 70, 255)
    
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)

    findContour(frame_clr, frameV)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frameV)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
