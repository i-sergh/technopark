import cv2
cap = cv2.VideoCapture (0)
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # red
    clr_low = (0, 210, 110)
    clr_high = (15,255,255)
    # green
    clr_low = (30, 110, 90)
    clr_high = (90,255,255)
    #yellow
    clr_low = (15, 100, 100)
    clr_high = (70,255,255)

    frame_clr = cv2.inRange (frame_HSV, clr_low, clr_high)
    cv2.imshow ('248', frame_clr)
    cv2.imshow ('548', frame)
    if cv2.waitKey (1) == ord ('q'):
        break
cap.release()
cv2.destroyAllWindows()
