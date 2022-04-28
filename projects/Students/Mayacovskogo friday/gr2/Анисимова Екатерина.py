import cv2

cap = cv2.VideoCapture( 0 )

def findContor( clr_mask, out):
    cont, h = cv2.findContours( clr_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)

    cv2.drawContours( out, cont, 0, (25,20,20), -1)

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    clr_low = (30, 55, 70)
    clr_high = (120, 200, 255)

    frame_clr = cv2.inRange(frame_HSV, clr_low,clr_high)
    findContor(frame_clr,frame)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame )
    if cv2.waitKey(1) == ord('q'):
         break
        
cap.relese()
cv2.destroyAllWindows()
