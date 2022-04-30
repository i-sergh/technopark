import cv2
import numpy as np
cnv = np.ones((480,640,3),dtype=np.uint8())
cap = cv2.VideoCapture(0)
def findCenter(frame_mask,out):
    moments=cv2.moments(frame_mask,1)
    m00=moments["m00"]
    m01=moments["m01"]
    m10=moments["m10"]
    if m00>100:
        x=int(m10/m00)
        y=int(m01/m00)
        cv2.circle(out,(x,y),5, (0,255,255),-1)
def findContour (frame_mask,out,cnv,clr):
    cont, h=cv2.findContours(frame_mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    cont= sorted(cont, key=cv2.contourArea,reverse=True)
    cv2.drawContours(out,cont,0,(0,255,0),2)
    cv2.drawContours(frame_mask,cont,0,(0,0,0),-1)
    cv2.drawContours(cnv,cont,0,clr,-1)
color_p=(0,255,0)
while True:
    rt, frame = cap.read()
    frame=cv2.flip(frame,2)
    frame_HSV=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    clr_low=(0, 160, 110)
    clr_high=(15, 255, 255)
    frame_clr=cv2.inRange(frame_HSV,clr_low,clr_high)
    #findCenter(frame_clr,frame)
    findContour(frame_clr,frame,cnv,color_p)
    findContour(frame_clr,frame,cnv,color_p)
    findContour(frame_clr,frame,cnv,color_p)
    findContour(frame_clr,frame,cnv,color_p)
    cv2.imshow("msck", frame_clr)
    cv2.imshow("frame",frame)
    cv2.imshow("paint",cnv)
    key=cv2.waitKey(1)
    if key ==ord("q"):
        break
    if key ==ord("z"):
        color_p=(255,0,0)
    if key ==ord("x"):
        color_p=(0,255,0)
    if key ==ord("c"):
        color_p=(0,0,255)
    if key ==ord("a"):
        color_p=(0,0,0)
    if key ==ord("v"):
        color_p=(100,50,200)
    if key ==ord("b"):
        color_p=(200,200,250)
    if key ==ord("n"):
        color_p=(0,255,255)
cv2.destroyAllWindows()
cap.releas()
