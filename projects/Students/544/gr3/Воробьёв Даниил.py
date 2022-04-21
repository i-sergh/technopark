import cv2
from random import randint
cap = cv2.VideoCapture ( 0 )

c_live_time = 10
i_live = c_live_time

while True:
     tr, frame = cap.read ()
     frame_HSV = cv2.cvtColor ( frame,
                                cv2.COLOR_BGR2HSV )
     clr_low = (0, 150, 110)
     clr_high = (40, 255, 255)

     frame_clr = cv2.inRange ( frame_HSV, clr_low, clr_high )
     if i_live >= c_live_time:
         center = ( randint (0 , 400), randint(0 , 400))
         radius = randint(1,80)
         color = (randint(0,225), randint(0,225),randint(0,225))
         i_live = 0
     cv2.circle( frame,  
                 center,
                 radius,
                 color,
                 -1 )
     
     cv2.imshow('mask', frame_clr )
     cv2.imshow('main', frame)

     if cv2.waitKey(1) == ord('q'):
         break

cap.release()
cv2.destroyAlWindows()
                              
