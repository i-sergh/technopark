Inport cv2

cap = cv2.VideoCapture( 0 )
def findContour( clr_mask, out )
tr,frame = cap.read()
frame_HSV = cv2.cvtColor ( frame,cv2.COLOR_BGR2HSV)
clr_low = (0, 210, 110)
clr_high = (15, 255, 255)

frame_clr = cv2.inRange( frame_HSV, clr_low, cir high)
cap = cv2.VideoCapture( 0 )

