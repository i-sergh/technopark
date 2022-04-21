import cv2

class Camera:
    def video(self):
        cap = cv2.VideoCapture(0)
        while True:
            tr, frame = cap.read()
            frame_HSV = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

            clr_low = (0, 210, 110)
            clr_hight = (15, 255, 255)
            
            frame_clr = cv2.inRange(frame_HSV, clr_low, clr_hight)

            cv2.imshow('window', frame)
            cv2.imshow('window_clr', frame_clr)

            if cv2.waitKey(1) == ord('q'):
                break
        cap.release()
        cv2.destroyAllWindows

cap = Camera()
cap.video()