import cv2
vid = cv2.VideoCapture('in.mp4')
while True:
    rt, frame = vid.read()
    if not rt:SV = cv2.cvtColorframe(frame, cv2.COLOR_BGR2HSV)
    clr_low = (0, 0, 160)
    clr_high = (180, 20, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    
        vid = cv2.VideoCapture('in.mp4')
        rt, frame = vid.read()
    cv2.imshw("mask", frame_clr)
    cv2.imshow('orig', frame)
    if cv2.waitKey(1) == ord('q'):
        break
vid.release()
cv2.destroyAllWindows()


