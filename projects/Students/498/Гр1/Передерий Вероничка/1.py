import cv2
cap=cv2.VideoCapture(0)
def findContour(mask_clr, out, clr_ch):
    cont, h,=cv2.findContours(mask_clr,
                              cv2.RETR_TREE,
                              cv2.CHAIN_APPROX_SIMPLE)
    cont=sorted(cont, key=cv2.contourArea, reverse=True)
    cv2.drawContours(out, cont, 0, clr_ch, -1)
img=cv2.imread('in.jpg')
color_Ch=(0,255,0)
while True:
    key=cv2.waitKey(1)
    rt, frame=cap.read()
    frameB=cv2.blur(frame,(5,5))
    frame_HSV=cv2.cvtColor(frameB,
                           cv2.COLOR_BGR2HSV)
    clr_low=(130,0,120)
    clr_high=(180,100,255)
    clr_low1=(0,0,120)
    clr_high1=(180,80,255)
    frame_clr=cv2.inRange(frame_HSV,
                          clr_low,
                          clr_high)
    frame_clr1=cv2.inRange(frame_HSV,
                          clr_low1,
                          clr_high1)
    if color_Ch:
        findContour(frame_clr + frame_clr1, frame, color_Ch)
    else:
        frame[frame_clr==255]=img[frame_clr==255]
    cv2.imshow('mask', frame_clr + frame_clr1)
    cv2.imshow('main', frame)
    if key==ord('q'):
        break
    if key==ord('z'):
        color_Ch=(0,255,0)
    if key==ord('x'):
        color_Ch=(0,255,255)
    if key==ord('c'):
        color_Ch=(200,50,100)
    if key==ord('v'):
        color_Ch=0
cap.release()
cv2.destroyAllWindows()

