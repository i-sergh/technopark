import cv2
tr, frame = cap.read()
frame_HSV = cv2.cvtColo
r ( frame, cv2.COIOR_BGR2HSV)
clr_low = (0,210,110)
cap = cv2.VideoCapture(0)
while True:
    tr, frame = cap.read()
    cv2.imshow( 'main', frame )
    if cv2.waitKey(1) == ord('g'):
        break
cv2.destroyAllWindows()
cap.release()
