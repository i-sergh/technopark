import cv2
import numpy as np
#import video

if __name__ =='__main__':
    def callback(*arg):
        print(arg)

cv2.namedWindow('webcam')

cap=cv2.VideoCapture(0)#create_capture(0)


hsv_min=np.array((40,55,100), np.uint8)
hsv_max=np.array((90,255,255), np.uint8)

while True:
    flag, img=cap.read()
    hsv=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    thresh=cv2.inRange(hsv,hsv_min, hsv_max)
   

    moments=cv2.moments(thresh,1)
    dM01=moments['m01']
    dM10=moments['m10']
    dArea=moments['m00']

    if dArea > 100:
        x=int(dM10/dArea)
        y=int(dM01/dArea)
        cv2.circle(img,(x,y),10,(0,0,255),-1)
    cv2.imshow('webcam', img)

    ch=cv2.waitKey(1)
    if ch==27:
        break

cap.release()
cv2.destroyAllWindows()
