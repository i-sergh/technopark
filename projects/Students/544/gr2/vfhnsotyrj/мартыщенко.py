import cv2

cap = cv2.VideoCapture( 0 )

vidoe = cv2.VideoCapture('night sky.mp4') 

while True:
    tr, frame = cap.read()
    tr, frameV = vidoe.read()
    
    if not tr:
        vidoe = cv2.VideoCapture('night sky.mp4')
        tr, frameV = video.read()




    
    frame_HSV = cv2.cvtColor(frameV,
                             cv2.COLOR_BGR2HSV)
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange (frame_HSV,
                             clr_low,
                             clr_high)
    
    cv2.imshow('video', frameV)
    
    cv2.imshow('mask', frame_clr)

    cv2.imshow('main', frame)

    if cv2.waitKey(91) == ord('q'):
        break

cap.release()
cv2.destroyAllWimdows()
