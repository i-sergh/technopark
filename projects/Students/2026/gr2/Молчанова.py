import cv2

cap = cv2.VideoCapture( 0 )

def findContour(clr_mask, out):
    cont, h = cv2.findContours(clr_mask,
                               cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    cv2.drawContours( out, cont, 0, (255, 255, 0), -1)

    try:
        m = cv2.moments (cont [0], 1)

        if m['m00'] > 100:
            x = int(m['m10'] / m['m00'])
            y = int(m['m01'] / m['m00'])

            cv2.circle(out, (x, y), 5, (0, 255, 2555), -1)
            return x, y            

    except:
        pass

while True:
    tr, frame = cap.read()

    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )

    clr_low_r = (0, 120, 110)
    clr_high_r = (15, 255,255)

    clr_low_y = (15, 120, 110)
    clr_high_y = (40, 255,255)

    clr_low_g = (40, 120, 110)
    clr_high_g = (90, 255,255)
    
    frame_clr_r = cv2.inRange( frame_HSV, clr_low_r, clr_high_r)
    frame_clr_y = cv2.inRange( frame_HSV, clr_low_y, clr_high_y)
    frame_clr_g = cv2.inRange( frame_HSV, clr_low_g, clr_high_g)
    print(findContour( frame_clr_r, frame ))
    findContour( frame_clr_y, frame )
    findContour( frame_clr_g, frame )

    #cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey( 1 ) == ord('q'):
        break

cap.release()
cv2.destroyALLWindows()
