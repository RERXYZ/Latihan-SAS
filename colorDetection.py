import cv2
import numpy as np

def detectColor(cam):
    while True:
        _, frame = cam.read();

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        lower = np.array([0,155,84])
        upper = np.array([13, 255, 255])

        mask = cv2.inRange(hsv, lower, upper)

        mask = cv2.medianBlur(mask, 7)

        contours, _= cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE) #check garis terluar kalau ketutup dia masuk

        for cnt in contours:
            area = cv2.contourArea(cnt) #menyimpan area 

            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt) #menyimpan variable x dan y

                cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2) #menandai di camera

                cv2.putText(frame, "Object Terdeteksi Bro", (x, y - 10), #dikasih text
                            cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("Utama", frame)
        cv2.imshow("Mask", mask)

        if cv2.waitKey(1) & 0xFF == ord('q'):
             break

    cam.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    cam = cv2.VideoCapture(0)

    detectColor(cam)
