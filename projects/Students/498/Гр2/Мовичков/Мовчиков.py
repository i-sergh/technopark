import cv2

cap = cv2.VideoCapture(0)

while True:
    rt, frame = cap.read()

    cv2.imshow('frame', frame)

    if cv2.waitkey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
