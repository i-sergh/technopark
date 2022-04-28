import cv2
cap=cv2.VideoCapture( 0 )
def findContour( clr_mask, out ):
    cont, h = cv2.findContours( clr_mask,
                                cv2.RETR_TREE,
                                cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted( cont, key=cv2.contourArea, reverse=True )
    cv2.drawContours(out, cont, contourIdx=0, color=(255,255,0),
                     thickness=2)
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame,
                             cv2.COLOR_BGR2HSV)
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)
    frame_reds = cv2.inRange( frame_HSV,
                              clr_low,
                              clr_high)
    findContour(frame_reds,frame)
    cv2.imshow( 'color mask', frame_reds)
    cv2.imshow( 'main', frame )
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
