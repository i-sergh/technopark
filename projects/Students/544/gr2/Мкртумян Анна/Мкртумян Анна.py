import cv2

cap = cv2.VideoCapture('traffic lights-4.mp4')

while True:
    #tr, frame = cap.read()

    tr, framev = cap.read()

    if not tr:
        cap = cv2.VideoCapture('traffic lights-4.mp4')
        tr, framev = cap.read()
    
    frame_HSV = cv2.cvtColor(framev, cv2.COLOR_BGR2HSV)

    clr_low = (0, 100, 80)
    clr_high = (40, 255, 255)

    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)

    cv2.imshow('mask', frame_clr)
    #cv2.imshow('main', frame)
    cv2.imshow('video', framev)

    

    if cv2.waitKey(1)== ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
