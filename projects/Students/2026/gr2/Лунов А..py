import cv2
global retcont, E
E = 0
retcont = []
cap = cv2.VideoCapture(0)
def findContour(clr_mask, out, clr_c):
    global X, Y, E
    global retcont
    cont, h = cv2.findContours(clr_mask,
                               cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont, key=cv2.contourArea, reverse=True)
    
    if len(cont)> 0:
        for sch,cn in enumerate(cont):
            if cv2.contourArea(cont[sch])> 300:
                
                if sch >= len(retcont):
                    
                    retcont.append(False)
                    
                else:
                    if E and cv2.pointPolygonTest(cont[sch], (X, Y), True) > 0:
                        retcont[sch] = not retcont[sch]
                if retcont[sch]:
                    cv2.drawContours(out, cont, 0, clr_c,-1)
                else: 
                    cv2.drawContours(out, cont, 0, clr_c,2)
    #return retcont

def mouse(event, x, y, flags, params):
    global X, Y, E
    X  = x
    Y = y
    E = event
    
cv2.namedWindow('main')
while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.setMouseCallback('main', mouse)

    clr_low = (0,0,200)
    clr_hight = (180, 255,255)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_hight)
    findContour(frame_clr,frame, (255,0,0))
    
    clr_low = (0,0,150)
    clr_hight = (180, 255,200)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_hight)
    findContour(frame_clr,frame, (0,255,0))
    
    clr_low = (0,0,80)
    clr_hight = (180, 255,150)
    frame_clr = cv2.inRange(frame_HSV, clr_low, clr_hight)
    findContour(frame_clr,frame, (0,0,255))

    
    
    cv2.imshow('mask', frame_clr)
    
    cv2.imshow('main', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()
