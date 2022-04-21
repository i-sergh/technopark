import sys
import numpy as np
import cv2 as cv

hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

fn = 'image.jpg'
img = cv.imread(fn)
hsv = cv.cvtColor( img, cv.COLOR_BGR2HSV )
thresh = cv.inRange( hsv, hsv_min, hsv_max )
_, coutours, hierarchy = cv.findCountours( thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

cv.drawConturs( img, contours, -1, (255,0,0), 3, cv.LINE_AA, hierarchy, 1)
cv.imshow('contours', img)

cv.waitKey()
cv.destroyALLWindows()
