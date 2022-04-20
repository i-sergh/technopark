import cv2


cap = cv2.VideoCapture(0)

def findCenter (frame, color_low, color_high, out):
    color_mask = cv2.inRange(frame, color_low, color_high)

    cont, h = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    try:
        cont = sorted(cont, key=cv2.contourArea, reverse=True)[0]

    
        moments = cv2.moments(cont, 1)

        m00 = moments['m00']
        m01 = moments['m01']
        m10 = moments['m10']
        if m00 >0:
            x = int(m10/m00)
            y = int(m01/m00)

            cv2.circle(out, (x, y), 5, (120,0,60), -1)

            return (x, y), color_mask
        return None, None
    except IndexError:
        return None, None

while True:
    rf, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    coordR, mask = findCenter (frame_HSV, (0,110,110), (15,255,255), frame)

    coordY, mask = findCenter (frame_HSV, (15,110,110), (40,255,255), frame)

    coordG, mask = findCenter (frame_HSV, (40,40,40), (120,255,255), frame)
    
    
    try:
        cv2.line(frame, coordY, coordR, (200,0,255), 1 )
    except:
        pass
    try:
        cv2.line(frame, coordG, coordR, (255,0,200), 1 )
    except:
        pass
   
    try:
        cv2.line(frame, coordY ,(coordY[0], coordG[1]), (255,0,200), 1 )
        cv2.line(frame, (coordY[0], coordG[1]), coordG, (200,0,255), 1 )
    except:
        pass
   
   
   # try:
    #    cv2.imshow('mask', mask)
    #except:
    #    pass
    cv2.imshow('main', frame)
    if cv2.waitKey(1) == 27:
        break
cv2.destroyAllWindows()
cap.release()