import cv2

cap = cv2.VideoCapture( 0 )

def findCenter(clr_mask, out):
    m = cv2.moments(clr_mask, 1 )
    m00 = m['m00']
    m01 = m['m01']
    m10 = m['m10']

    if m00 > 100:
        x = int( m10 / m00 )
        y = int( m01 / m00 )
        
        cv2.circle( out, (x, y), 5, (0,255,255), -1)
        return x, y
    else:
        return None, None
        
def findContour( clr_low, clr_high ,frame_HSV, out ):
    clr_mask = cv2.inRange( frame_HSV, clr_low, clr_high )
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE )
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,255,0), 2)
    try:
        findCenter(cont[0], out)
    except:
        pass

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV )
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)

    clr_low = (15, 150, 110)
    clr_high = (40, 255, 255)

    clr_low = (40, 65, 65)
    clr_high = (80, 255, 255)

    
    
    findContour(clr_low,clr_high,frame_HSV,frame )
    
    #cv2.imshow('mask', frame_clr )
    cv2.imshow( 'main', frame )

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()    
