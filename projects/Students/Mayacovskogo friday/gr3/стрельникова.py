import cv2

cap = cv2.VideoCapture(0)

def fintCenter (clr_mask, out):
    modules = cv2.moments(clr_mask, 1)

    m00 = modules['m00']
    m01 = modules['m01']
    m10 = modules['m10']

    if m00 >100:
        x = int(m10/m00)
        y = int(m01/m00)

        cv2.circle(out, (x, y), 5, (0, 255, 255), -1)

def findContour (clr_mask, out):

    cont, h = cv2.findContours(clr_mask,
                               cv2.RETR_TREE,
                               cv2.CHAIN_APPROX_SIMPLE)
    cont = sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours(out, cont, 0, (0, 255, 0, 0), 2)
    #out[cont[0] == 255]= 100

while True:
    tr, frame = cap.read()
    frame_HSV = cv2.cvtColor (frame,
                              cv2.COLOR_BGR2HSV)
    #красный
    clr_low = (0, 40, 90)
    clr_high = (40, 255, 255)

    frame_clr = cv2.inRange(frame_HSV,
                            clr_low,
                            clr_high)
    
    findContour (frame_clr, frame)
    
    cv2.imshow('color mask', frame_clr)
    cv2.imshow('main', frame)
    
    key = cv2.waitKey(1)
    if cv2.waitKey(1) == ord('q'):
        break
    if key == ord('s'):
        cv2.imwrite('screen.jpd', frame)

cap,release()
cv2.destroyAllWindows()
