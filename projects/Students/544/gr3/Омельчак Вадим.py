import cv2
from random import randint
cap = cv2.VideoCapture(0)
Dlive = 100
Alive = Dlive
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame,
                             cv2.COLOR_BGR2HSV)
    clr_low = (0, 150, 110)
    clr_high = (15, 255, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    if Alive >= Dlive:
        center = (randint(0, 400), randint(0, 400))
        radius = randint(20, 40)
        color = (randint(0, 255), randint(0, 255), randint(0, 255))
        Alive = 0
    cv2.circle(frame, center, radius, color, -1)
    Alive += 1
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
