import cv2

cap= cv2.VideoCapture(0)

def findCentre (frame_mask,out, txt='x'):
    moments=cv2.moments(frame_mask,1)

    m00=moments['m00']
    m01=moments['m01']
    m10=moments['m10']
    
    if m00>100:
        x=int(m10/m00)
        y=int(m01/m00)

        cv2.circle( out, (x,y), 5, (0,255,255), -1)
        cv2.putText(out, txt, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 2, (0,255,255), 2)

def findContour (frame_mask, out, txt=None ):
    cont,h = cv2.findContours(frame_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours( out, cont, 0, (0,255,0), 2)

    if len(cont):
        findCentre(cont[0], out, txt)
l_clrs= ['red','yellow','green']   
while True:
    rt, frame=cap.read()
    frame_HSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #red
    clr_low=(0,210,110)
    clr_high=(5,255,255)

    frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)

    findContour( frame_clr, frame, l_clrs[0])
    #orange
    #clr_low=(4,110,70)
    #clr_high=(15,255,255)
    #frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)

    #findContour( frame_clr, frame)
    #yellow
    clr_low=(15,210,110)
    clr_high=(30,255,255)
    frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)

    findContour( frame_clr, frame, l_clrs[1])
    #green
    clr_low=(30,210,70)
    clr_high=(120,255,255)
    frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)

    findContour( frame_clr, frame, l_clrs[2])
    #blue
    
    #frame_clr=cv2.inRange(frame_HSV, clr_low, clr_high)

    #findContour( frame_clr, frame)
    
    cv2.imshow('mask', frame_clr)    
    cv2.imshow('main', frame)

    if cv2.waitKey(1)==ord('q'):
        break

cap.realease()
cv2.destroyAllWindows()

    
