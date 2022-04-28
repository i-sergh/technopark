import cv2

cap = cv2.VideoCapture(0)
def findCenter(cir_mask,out):
    m=cv2.moments(cir_mask,1)
    m00=m['m00']
    m01=m['m01']
    m10=m['m10']
    if m00>100:
        x=int(m10/m00)
        y=int(m01/m00)
        cv2.circle(out, (x,y), 5, (0,255,255),-1)
 
def findContour(cir_mask,out):
    cont,h=cv2.findContours(cir_mask,
                             cv2.RETR_TREE,
                             cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours(out, cont, 0,(0,255,0),2)

while True:
    tr,frame=cap.read()
    frame_HSV=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    cir_low=(0,210,110)
    cir_high=(15, 255, 255)

    frame_cir=cv2.inRange(frame_HSV, cir_low, cir_high)
    findContour(frame_cir,frame)

    cv2.imshow('mask', frame_cir)
    cv2.imshow('main', frame)

    cv2.imshow('main', frame)
    
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
