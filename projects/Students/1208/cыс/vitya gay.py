import cv2

cap=cv2.VideoCapture(0)

def findCenter(clr_mask, out):
    moments=cv2.moments(clr_mask, 1)

    m00=moments['m00']
    m01=moments['m01']
    m10=moments['m10']

    if m00 > 100:
        x=int(m10/m00)
        y=int(m01/m00)

        cv2.circle(out, (x,y), 5, (255,255,0), -1)

def findContour(clr_mask, out, color=(0,255,0)):
    cont, h=cv2.findContours(clr_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont,key=cv2.contourArea, reverse=True)
    try:
        findCenter(cont[0],out)
    except:
        pass

    cv2.drawContours(out, cont, 0, color, 2)
    cv2.drawContours(clr_mask, cont,0,(0,0,0),-1)

while True:
    tr, frame=cap.read()
    frame_=cv2.blur(frame,(10,10))
    frame_HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    clr_low=(15,159,100)
    clr_high=(40,255,255)
    clr_low1=(40,120,70)
    clr_high1=(120,255,255)
    clr_low2=(140,110,100)
    clr_high2=(165,255,255)
    clr_low3=(0,150,100)
    clr_high3=(15,255,255)
    
    
    
    frame_clr=cv2.inRange(frame_HSV,clr_low,clr_high)
    frame_clr1=cv2.inRange(frame_HSV,clr_low1,clr_high1)
    frame_clr2=cv2.inRange(frame_HSV,clr_low2,clr_high2)
    frame_clr3=cv2.inRange(frame_HSV,clr_low3,clr_high3)

    findCenter(frame_clr, frame)
    
    findContour(frame_clr,frame)
    findContour(frame_clr,frame, (0,125,255))
    findContour(frame_clr1,frame, (0,125,123))
    findContour(frame_clr2,frame, (0,125,255))
    findContour(frame_clr3,frame, (0,125,123))
    cv2.imshow('ha4', frame)
    cv2.imshow('wevcam',frame_clr)
    if cv2.waitKey(1)==ord('q'):
        break

cv2.destroyAllWindows()
cap.release()
