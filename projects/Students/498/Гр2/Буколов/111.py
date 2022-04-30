import cv2

cap = cv2.VideoCapture(0)

def findCenter (frame_mask, out, txt):
    moments = cv2.moments( frame_mask, 1)

    m00 = moments['m00']
    m01 = moments['m01']
    m10 = moments['m10']

    if m00 > 100:
        x = int(m10 / m00)
        y = int(m01 / m00)

        cv2.circle ( out, (x,y), 5, (0,255, 255), -1)
        #cv2.putText( out, txt, (x,y), cv2.FONT
def findContour (frame_mask, out, txt):
    cont, h = cv2.findContours ( frame_mask,
                                 cv2.RETR_TREE,
                                 cv2.CHAIN_APPROX_SIMPLE)

    cont = sorted(cont,key=cv2.contourArea,reverse=True)
    for cn in cont:
        if cv2.contourArea(cn)<1000:
            break
        cv2.drawContours(out, cont, -1, (0,255,0), 2)
        findCenter(cn,out, txt)
l_color = ['red', '
while True:
    rt, frame = cap.read()
    frame_HSV = cv2.cvtColor( frame,
                              cv2.COLOR_BGR2HSV )
    #красный
    clr_low = (0, 200, 110)
    clr_high = (15, 255, 255)

    frame_clr = cv2.inRange ( frame_HSV,
                              clr_low,
                              clr_high )
    findContour(frame_clr, frame, 't')
    #зелёный
    clr_low = (40, 120, 20)
    clr_high = (140, 255, 255)

    frame_clr = cv2.inRange ( frame_HSV,
                              clr_low,
                              clr_high )
    findContour(frame_clr, frame, 't')

    #синий
    clr_low = (80, 110, 110)
    clr_high = (140, 255, 255)

    frame_clr = cv2.inRange ( frame_HSV,
                              clr_low,
                              clr_high )
    findContour(frame_clr, frame, 't')
    #фиолетовый
    clr_low = (140, 110, 100)
    clr_high = (165, 255, 255)

    frame_clr = cv2.inRange ( frame_HSV,
                              clr_low,
                              clr_high )
    findContour(frame_clr, frame, 't')
    cv2.imshow('msck', frame_clr)
    cv2.imshow('frame', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
cap.release()    
