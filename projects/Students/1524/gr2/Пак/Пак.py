import cv2

video = cv2.VideoCapture('video.mp4')

while True:
    rt, frame = video.read()
    
    if not rt:
        video = cv2.VideoCapture('video.mp4')
        rt, frame = video.read()

    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    clr_red_low = (0 // 2, 0, 75)
    clr_red_high = (80 // 2, 255, 255)
    clr_red_low_anlg = (300 // 2, 0, 75)
    clr_red_high_anlg = (360 // 2, 255, 255)
    clr_ylw_low = (20 // 2, 50, 75)
    clr_ylw_high = (40 // 2, 255, 255)
    clr_grn_low = (130 // 2, 50, 75)
    clr_grn_high = (170 // 2, 255, 255)

    frame_clr_red = cv2.inRange(frame_HSV, clr_red_low, clr_red_high)
    frame_clr_red_anlg = cv2.inRange(frame_HSV, clr_red_low_anlg, clr_red_high_anlg)
    frame_clr_ylw = cv2.inRange(frame_HSV, clr_ylw_low, clr_ylw_high)
    frame_clr_grn = cv2.inRange(frame_HSV, clr_grn_low, clr_grn_high)
    
    cv2.imshow('original', frame)
    cv2.imshow('red', frame_clr_red + frame_clr_red_anlg )
    cv2.imshow('yellow', frame_clr_ylw)
    cv2.imshow('green', frame_clr_grn)

    if cv2.waitKey(1) == ord('q'):
        break

video.release()
cv2.deastroyAllWindows
