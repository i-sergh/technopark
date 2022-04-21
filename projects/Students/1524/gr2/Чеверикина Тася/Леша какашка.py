import cv2
vid=cv2.VideoCapture("in.mp4")

while True:
    rt, frame=vid.read()
    if not rt:
        vid=cv2.VideoCapture("in.mp4")
        rt,frame=vid.read()
    frame_HSV=cv2.cvtColor( frame,
                            cv2.COLOR_BGR2HSV)
    clr_low=(0, 0, 160)
    clr_high= (180, 80, 255)

    frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)
        
    cv2.imshow("mask",frame_clr)
    cv2.imshow("orig",frame)
    if cv2.waitKey(1)==ord("q"):
        break
vid.release()
cv2.destroyAllWindows()

