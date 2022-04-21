import cv2

cap = cv2. VideoCapture ( 0 )

video = cv2.VideoCapture( 'Golf Course.mp4' )

while True:
    tr, frame = cap.read()

    tr, frameV = video.read()
    if not tr:
        video = cv2.VideoCapture( 'Golf Course.mp4' )
        tr, frameV = video.read()
    
    frame_HSV = cv2.cvtColor(frameV,
                             cv2.COLOR_BGR2HSV)
    clr_low = (30, 110, 60)
    clr_high = (90, 255, 255)

    frame_clr = cv2.inRange(frame_HSV,
                            clr_low,
                            clr_high)
    
    cv2.imshow('video', frameV)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey(1)  == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
