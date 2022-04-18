import cv2

cap = cv2.VideoCapture(0)

def findCenter(frame_mask,out):
    moments=cv2.moments(frame_mask,1)

    m00=moment['m00']
    m01=moment['m01']
    m10=moment['m10']



def findContour(frame_mask,out):
    cont,h=cv2.findContours(frame_mask,
                           cv2.RETR_TREE,
                           cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont,key=cv2.contourArea,reverse=True)

    cv2.drawContours(out,cont,0,(0,255,0),-1)

while True:
    rt,frame = cap.read()
    frame_HSV=cv2.cvtColor(frame,
                           cv2.COLOR_BGR2HSV)
    # Red
    clr_low=(0,160,110)
    clr_high=(15,255,255)

    clr_low =()
    clr_high=()

    frame_clr=cv2.inRange(frame_HSV,
                          clr_low,
                          clr_high)
    findContour(frame_clr,frame)                   
    cv2.imshow('msck',frame_clr)
    cv2.imshow('frame',frame)

    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyALLWindows()
cap.release()
