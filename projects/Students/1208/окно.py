import cv2
cap = cv2.VideoCapture(0)

def oleg(frame_clr,out):
    cont,h=cv2.findContours(frame_clr,
                            cv2.RETR_TREE,
                            cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont,key=cv2.contourArea,reverse=True)
    cv2.drawContours(out,cont,0,(0,255,0),2)

    if len(cont):
        moments=cv2.moments(cont[0],1)

        m00=moments['m00']
        m01=moments['m01']
        m10=moments['m10']

        if m00>100:
            x=int(m10/m00)
            y=int(m01/m00)
            cv2.circle(out,(x,y),5,(0,255,255),-1)

while True:
    tr, frame = cap.read()
    frame_=cv2.blur(frame,(20,20))
    frame_HSV=cv2.cvtColor(frame_,cv2.COLOR_BGR2HSV)

#красный
    clr_low=(0,200,110)
    clr_high=(15,255,255)

    frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)
    oleg(frame_clr,frame)
#желтый
    clr_low2=(15,200,100)
    clr_high2=(40,255,255)

    frame_clr=cv2.inRange(frame_HSV, clr_low2, clr_high2)
    oleg(frame_clr,frame)
#зеленый
    clr_low3=(40,120,40)
    clr_high3=(120,255,255)

    frame_clr=cv2.inRange(frame_HSV, clr_low3, clr_high3)
    oleg(frame_clr,frame)
#фиолетовый
    clr_low4=(140,110,70)
    clr_high4=(170,255,255)

    frame_clr=cv2.inRange(frame_HSV, clr_low4, clr_high4)

    oleg(frame_clr,frame)
    
    cv2.imshow('grysha',frame_clr)
    cv2.imshow('main', frame)

    if cv2.waitKey(1) == ord('q'):
        break




cv2.destroyAllWindows()
cap.release()
        
