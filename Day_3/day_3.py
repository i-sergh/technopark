import cv2
import numpy as np


cap = cv2.VideoCapture(0)

def find_dot (color_mask, cnv):
    
    moments = cv2.moments(color_mask, 1)
    dM01 = moments['m01']
    dM10 = moments['m10']
    dArea = moments['m00']

    if dArea > 100:
        #print(dM10)
        x = int(dM10 / dArea)
        y = int(dM01 / dArea)
        cv2.circle(cnv, (x, y), 10, (0,0,255), -1)

def draw_rect(color_mask, cnv):
    contours, hierarchy = cv2.findContours( color_mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    
    try:
        cv2.drawContours( cnv, contours, 0, (0,255,0), 3, cv2.LINE_AA, hierarchy, 1 )
    except:
        pass

while True:
    ret, frame = cap.read()
    # HSV max is 180 255 255
    frame_HSV = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV) 
    #print(np.max(frame_HSV[:,:,1]))
    
    #Лицо + красный 
    #red_low = (4,66,183)
    #red_high = (30,214,255)
    
    # красный 
    red_low = (0,140,160)
    red_high = (20,255,255)

    # желтый *помехи*
    yellow_low = (25, 7, 100)
    yellow_high = (30, 255, 255)
    
    # Синий 
    blue_low = (110, 205, 76)
    blue_high = (115, 230, 255)

    # Зелёный 
    green_low = (55, 1, 86)
    green_high = (65, 130, 255)

    
    red_in_frame = cv2.inRange(frame_HSV, red_low, red_high)

    

    yellow_in_frame = cv2.inRange(frame_HSV, yellow_low, yellow_high)
    blue_in_frame = cv2.inRange(frame_HSV, blue_low, blue_high)
    green_in_frame = cv2.inRange(frame_HSV, green_low, green_high)
    
    find_dot(red_in_frame, frame)
    draw_rect(red_in_frame, frame)

    cv2.imshow('original', frame )
    cv2.imshow('red', red_in_frame )
    cv2.imshow('yellow', yellow_in_frame )
    cv2.imshow('blue', blue_in_frame )
    cv2.imshow('green', green_in_frame )
    if cv2.waitKey(1) == ord('q'):
        break



cap.release()
cv2.destroyAllWindows()
