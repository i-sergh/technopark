import cv2

cap=cv2.VideoCapture(0)
def findCenter(clr_mask,out):
    m=cv2.momemts(clr_mask,1)
    m00=m['m00']
    m01=m['m01']
    m10=m['m10']

    if m00>100:
        x=int(m10/m00)
        y=int(m01/m00)

        cv2.circle(out,(x,y),5,(0,255,255),-1)
    

def findContour(clr_mask, out):
    cont,h=cv2.findContours(clr_mask,cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont,key=cv2.contourArea,reverse=True)
    cv2.drawContours(out,cont,0,(0,255,0),2)
    try:
        findCenter(cont[0],out)
    except:pass

while True:
    tr,frame=cap.read()
    frame_HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    clr_low=(0,210,110)
    clr_high=(15,255,255)

    clr_low2=(0,128,0)
    clr_high2=(0,128,0)

    clr_low3=(0,80,0)
    clr_high3=(50,255,80)

    frame_clr=cv2.inRange(frame_HSV,clr_low,clr_high)
    findContour(frame_clr,frame)
   
    frame_clr2=cv2.inRange(frame_HSV,clr_low2,clr_high2)
    
    frame_clr3=cv2.inRange(frame_HSV,clr_low3,clr_high3)
    findContour(frame_clr3,frame)
    
    cv2.imshow('mask',frame_clr3)
    cv2.imshow('main',frame)

    if cv2.waitKey(1)==ord('q'):
        break
cap,release()
cv2.destroyAllWindows()
