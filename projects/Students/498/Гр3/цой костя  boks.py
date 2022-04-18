import cv2
cap=cv2.VideoCapture(0)
def findcontour (frame_mask, out):
    cont, h=cv2.findContours (frame_mask,
                              cv2.RETR_TREE,
                              cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours(out, cont, 0, (0,255,0),2)
while True:
    rt, frame =cap.read()
    frame_HSV=cv2.cvtColor (frame,
                            cv2.COLOR_BGR2HSV)
    clr_low=(15, 160, 110)
    clr_high=(30, 255, 255)
    frame_clr=cv2.inRange(frame_HSV,
                          clr_low,
                          clr_high)
    findcontour( frame_clr, frame)
    cv2.imshow('main', frame)
    cv2.imshow('hey', frame_clr)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
