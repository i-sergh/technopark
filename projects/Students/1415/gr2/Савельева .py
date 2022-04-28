import cv2

cap = cv2.VideoCapture(0)

img = cv2.imread("in.jpg")
cv2.imshow("image", img)
while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame,
                                 cv2.COLOR_BGR2HSV)
    clr_low = (0, 110, 70)
    clr_high = (40, 255, 255)
    frame_clr = cv2.inRange(frame_HSV,
                                clr_low, clr_high)
    
    cv2.imshow("main b4 change", frame)
    frame[frame_clr == 255] = img[frame_clr == 255]
    cv2.imshow("after change", frame)
    cv2.imshow('color-mask', frame_clr)
    if cv2.waitKey(1) == ord("q"):
        break

