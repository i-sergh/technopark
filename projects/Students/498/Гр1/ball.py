import cv2
import numpy as np
from random import randint

class Ball:
    def __init__ (self,  x, y, r, clr):
        #self.cnv = cnv
        self.x = x
        self.y = y
        self.r = r
        self.clr = clr
        self.vx = randint(-20,20)
        self.vy = randint(-20,20)
        #print(self.vx, self.vy)
        self.back_clr = (1,1,1)
        
    def draw(self, cnv):
        cv2.circle( cnv, (self.x,self.y), self.r, self.clr, -1 )
        
    def destroy(self,cnv):
        cv2.circle( cnv, (self.x,self.y), self.r, self.back_clr, -1 )

    def move(self,cnv ):
        #print(self.vx, self.vy)
        self.destroy(cnv)
        
        if self.x + self.vx + self.r  > cnv.shape[1]:
            self.vx *= -1
            
            if abs(self.vx) > 2:
               self.vx  = int(self.vx*0.9)
               

        if self.x + self.vx - self.r  < 0:
            self.vx *= -1
            if abs(self.vx) > 2:
               self.vx  = int(self.vx*0.9)

        if self.y + self.vy + self.r  > cnv.shape[0]:
            self.vy *= -1
            if abs(self.vy) > 2:
               self.vy  = int(self.vy*0.9)

        if self.y + self.vy - self.r  < 0:
            self.vy *= -1
            if abs(self.vy) > 2:
               self.vy  = int(self.vy*0.9)
        self.x += self.vx
        self.y += self.vy
    
        self.draw(cnv)
        
    def giveVelocity(self, vx, vy):
        self.vx += vx
        self.vy += vy
        
if __name__ == '__main__':
    cnv = np.ones( (600, 600, 3), dtype=np.uint8() )

    ball = Ball( 300+ randint(0,100), 300+ randint(0,100), 50, (0,255,255))

    while True:

        ball.move(cnv)
        cv2.imshow('main', cnv)
            
        key = cv2.waitKey(1)
        if key == 27:
            break
        if key == ord('w'):
            ball.giveVelocity(2, 0)
        if key == ord('s'):
            ball.giveVelocity(-2, 0)
        if key == ord('a'):
            ball.giveVelocity(0, -2)
        if key == ord('d'):
            ball.giveVelocity(0, 2)
    
    cv2.destroyAllWindows()
