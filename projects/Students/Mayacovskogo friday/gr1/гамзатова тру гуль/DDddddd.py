import cv2

cap = cv2.VideoCapture(0)

def findCenter(mask_clr, out):
    moments = cv2.moments(mask_clr, 1)
    m00 = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']

    if m00 > 100:
        x = int(m10/m00)
        y = int(m01/m00)
        cv2.circle(out,(x,y), 5, (200,0,255),-1)
        return (x,y)
def findContour(mask_clr, out):

    cont, h = cv2.findContours(mask_clr,
                               cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key = cv2.contourArea, reverse=True)

    cv2.drawContours(out, cont, 0, (0, 255,0), 2)
    if len(cont)> 0:
        coord = findCenter(cont[0], out)
        return (coord, cont[0])
    return (None, None)
while True:
    tr,frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    
                            
    clr_low = (15, 150, 110)
    clr_high = (40, 255, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    coordY, contY = findContour(frame_clr, frame)

    clr_low = (40, 120, 70)
    clr_high = (120, 255, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    coordG, contG = findContour(frame_clr, frame)
    
    clr_low = (140, 110, 100)
    clr_high = (165, 255, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high ) 
    coordP, contP = findContour(frame_clr, frame)
    
    clr_low = (0, 150, 110)
    clr_high = (15, 255, 255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_high)
    coordR, contR =  findContour(frame_clr, frame)
    if coordY and coordG:
        cv2.line(frame, coordY, coordG, (200,0,100), 2)

    if coordG and coordP:
        cv2.line(frame, coordG, coordP, (200,0,100), 2)

    if coordP and coordR:
        cv2.line(frame, coordP, coordR, (200,0,100), 2)

    
    if coordR and coordY:
        cv2.line(frame, coordR, coordY, (200,0,100), 2)

    
    
    cv2.imshow('mask', frame_clr)
    cv2.imshow('main',frame)

    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
cap.release()

                         
