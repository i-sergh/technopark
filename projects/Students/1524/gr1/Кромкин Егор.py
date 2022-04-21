import cv2
cap = cv2.VideoCapture(0)
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    clr_l = (0, 210, 110)
    clr_h = (15, 255, 255)
    frame_clr1 = cv2.inRange(frame_HSV, clr_l, clr_h)

    clr_l = (90, 210, 110)
    clr_h = (150, 255, 255)
    frame_clr2 = cv2.inRange(frame_HSV, clr_l, clr_h)

    clr_l = (40, 90, 25)
    clr_h = (80, 255, 255)
    frame_clr3 = cv2.inRange(frame_HSV, clr_l, clr_h)
    
    cv2.imshow("main", frame)
    cv2.imshow("min", frame_clr1 + frame_clr2 + frame_clr3 )
    if cv2.waitKey(1) == ord("q"):
        break
cap.release()
cv2.destroyAllWindows()
