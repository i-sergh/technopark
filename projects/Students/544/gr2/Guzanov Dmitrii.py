import cv2
cap = cv2.VideoCapture (0)
video = cv2.VideoCapture('Night sky.mp4')
while True:
    tr, frame = cap.read()
    frame_clr = cv2.cvtColor(frame, cv2.COLOR_BGR2HCL)
    clr_low = (0, 210, 110)
    clr_high = (15, 255,255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    if cv2.waitKey(1) == ord('q'):
        break
 cap.release()
cv2.destroyAllWindows()
