import cv2
cap = cv2.VideoCapture( 'in.mp4' )

def findCenter (clr_mask, cnv):

    moments = cv2.moments(clr_mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(cnv, (x, y), 10, (0,0,255), -1)
        cv2.putText( cnv, str( dArea ), (x, y),cv2.FONT_HERSHEY_DUPLEX, 1,(0,100,0), 2 )

def findContour(color_mask, out):
    cont, h = cv2.findContours(color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cont = sorted(cont, key = cv2.contourArea, reverse = True)

    try:
        cv2.drawContours(out, cont, contourIdx=0, color=(0,255,0), thickness=1)

        findCenter(cont[0], out)

    except:
        pass

while True:
    tr, frame = cap.read()
    if not tr:
        cap = cv2.VideoCapture( 'in.mp4' )
        tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
    clr_low = (0, 0, 110)
    clr_high = (180, 40, 255)

    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    findContour(frame_clr, frame)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()

cap.release()
