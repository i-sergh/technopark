import cv2
from random import randint
cap = cv2.VideoCapture( 0 )

def findCenter (mask_clr, out):
    moments = cv2.moments(mask_clr, 1 )
    m00 = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']

    if m00 > 100:
        x = int( m10 / m00 )
        y = int( m01 / m00 )
        cv2.circle( out, (x, y), 5, (200, 0, 255), 1 )
        pizza(out,x, y )

def pizza (out, x, y):
    cv2.circle( out, (x, y), 100, (0, 0, 223), -1 )
    #cv2.circle( out, (x+100, y-100), 100, (155, 155, 223), 85 )
    cv2.circle( out, (x-10, y-10), 100, (0, 100, 248), 30 )
    for i in range (9):
          cv2.circle( out, (x+ randint(-80, 80)  , y+ randint(-80, 80) ), 10, (50, 100, 173), -1 )
    
def findContour ( mask_clr, out ):

    cont, h = cv2.findContours( mask_clr,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont, key=cv2.contourArea, reverse=True )

    cv2.drawContours( out, cont, 0, (0,255,0), 1 )
    if len(cont) > 0:
        findCenter(cont[0], out)

   

    
while True:
    tr,frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )

    clr_low = (0, 150, 110)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high )

    findContour( frame_clr, frame )
    
    cv2.imshow('mask', frame_clr  )
    cv2.imshow('main', frame )

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.relese()
