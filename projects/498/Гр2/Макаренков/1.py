import cv2

cap = cv2.VideoCapture (0)

def findCenter (frame_mask, out):
    moments=cv2.moments(frame_mask,1)

    m00=moment["m00"]
    m01=moment["m01"]
    m10=moment["m10"]

    if m00>100:
        x=int(m10/m00)
        y=int(m01/m00)

        cv2.circle(out(x,y),5,(0,255,255),-1)

def findContour (mask_clr, out):
    cont,h, = cv2.findContours (mask_clr,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)

    cont = sorted(cont, key=cv2.contourArea,reverse=True)
    cv2.drawContours (out, cont,  (0,255,0), 2)

while True:
    rt,frame = cap.read()
    frame_HSV = cv2.cvtColor (frame,
                              cv2.COLOR_BGR2HSV)

    clr_low = (0, 200, 110)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange (frame_HSV,
                             clr_low,
                             clr_high)
    findCenter(frame_clr,frame)
    findContour(frame_clr,frame)
    cv2.imshow ('mask', frame_clr)
    cv2.imshow ('main', frame)

    if cv2.waitKey(1)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
    
