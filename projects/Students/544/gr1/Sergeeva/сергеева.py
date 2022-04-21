import cv2
cap = cv2.VideoCapture ( 0 )

img = cv2.imread('akne3.jpg')

while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor ( img, cv2.COLOR_BGR2HSV)
    
    clr_low = (0, 210, 110)
    clr_high = (15, 255, 255)
    
    clr_low = (0, 0, 0)
    clr_high = (160, 84, 100)
    

    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)

    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)
    cv2.imshow('izo', img )
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
