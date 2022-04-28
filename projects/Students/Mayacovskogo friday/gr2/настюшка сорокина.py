import cv2

cap = cv2.VideoCapture( 0 )

def findContour( clr_mask, out ):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE )
    cont = sorted(cont, key=cv2.contourArea,reverse=True)

    cv2.drawContours( out, cont, 0, (0,255,0), 2)

    try:
        moments = cv2.moments(cont[0], 1)

        m00 = moments['m00']

        return m00
    except:
        return 0

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV)
    clr_low = (0, 150, 110 )
    clr_high = (15, 255, 255)
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    r = findContour(frame_clr, frame)
    
    clr_low = (15, 150, 110 )
    clr_high = (40, 255, 255)
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    y = findContour(frame_clr, frame)
    
    clr_low = (30, 110, 70 )
    clr_high = (90, 255, 255)
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    g = findContour(frame_clr, frame)

    mx = max([r, y, g])
    if mx == r:
        print('спелый')
    elif mx == y:
        print ('почти')
    else:
        print('незрелый')
    
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()



