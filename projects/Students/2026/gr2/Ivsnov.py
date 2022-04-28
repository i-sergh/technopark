import cv2

cap = cv2.VideoCapture( 0 )

def findContour(clr_mask, out):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,0,255), 2,)

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame, cv2.COLOR_BGR2HSV )
    clr_low = (0, 210, 0)
    clr_high = (180, 255, 255)


    clr_low = (0, 110, 0)
    clr_high = (180, 210, 255)
    clr_low = (0, 110, 0)
    clr_high = (180, 110, 255)
    clr_low = (0, 0, 0)
    clr_high = (180, 55, 255)
    frame_clr = cv2.inRange( frame_HSV, clr_low, clr_high)
    findContour( frame_clr, frame )
    cv2.imshow('mask', frame_clr )
    cv2.imshow('main', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
