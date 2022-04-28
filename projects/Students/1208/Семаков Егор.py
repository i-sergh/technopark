import cv2

cap=cv2.VideoCapture(0)


def findContour ( frame_clr, out):
    cont, h = cv2.findContours (frame_clr,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours (out, cont, 0, (0,255,0), 2)
    if len(cont):
        moments=cv2.moments(cont[0],1)

        m00 = moments['m00']
        m01 = moments['m01']
        m10 = moments['m10']

        if m00>0:
            x = int(m10/m00)
            y = int(m01/m00)
            cv2.circle(out, (x,y), 5, (0,255,255),-1)
    
while True:
    tr, frame = cap.read()
    frame_=cv2.blur(frame,(10,10))
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    
    clr_low = (0, 150, 100)
    clr_high = (15,255,255)

    clr_low1 = (40, 110, 70)
    clr_high1 = (90,255,255)

    clr_low2 = (15, 150, 110)
    clr_high2 = (40,255,255)

    clr_low3 = (90, 150,100)
    clr_high3 = (140,255,255)
    
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)

    frame_clr1 = cv2.inRange(frame_HSV, clr_low1, clr_high1)

    frame_clr2 = cv2.inRange(frame_HSV, clr_low2, clr_high2)

    frame_clr3 = cv2.inRange(frame_HSV, clr_low3, clr_high3)
    
    findContour(frame_clr,frame )

    findContour(frame_clr1,frame )

    findContour(frame_clr2,frame )

    findContour(frame_clr3,frame )
    
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
