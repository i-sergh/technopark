import cv2
import numpy as np
cap = cv2.VideoCapture(0)


def findCenter(mask_clr, out):
    moments = cv2.moments(mask_clr, 1)
    m00 = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']

    if m00 > 100:
        x = int(m10/m00)
        y = int(m01/m00)
        cv2.circle(out, (x, y), 5, (200, 0, 255), -1)

def findContour(mask_clr, out):

    cont, h = cv2.findContours(mask_clr,
                               cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    
    cv2.drawContours(out, cont, 0, (255, 200,100), 1)
    cnv = np.zeros((480,640),dtype=np.uint8() )
    if len(cont) >0:
        findCenter(cont[0], out)
        cv2.drawContours(cnv, cont, 0, (255, 255,255), -1)
    return cnv

while True:
    tr,frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    clr_low = (0, 0, 0)
    clr_high = (180, 255, 70)

    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)

    cnv = findContour(frame_clr, frame)

    frame[cnv==255,:]=(100, 0, 255)
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main',frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
       
    
