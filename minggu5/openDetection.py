import cv2;
import numpy as np
    
def openDetection(cam):
    while True:
        _, frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([0,0,2])
        upper = np.array([10 ,68,92])

        mask = cv2.inRange(hsv, lower, upper)

        mask = cv2.medianBlur(mask, 7)

        contours , _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
                cv2.putText(frame,"Jomok terdeteksi!",(x,y-10),
                        cv2.FONT_HERSHEY_SIMPLEX,0.9,(0,255,0),2)
        cv2.imshow('Detection', frame)
        cv2.imshow('Mask', mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
    openDetection(cam)
    pass