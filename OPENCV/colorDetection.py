import cv2
import numpy as np

def detectorColor(Kam):
    while True:
        _, prame= Kam.read()
        hsv = cv2.cvtColor(prame, cv2.COLOR_BGR2HSV)
        tinggi = np.array([140, 0,215])
        rendah = np.array ([160, 45,255])
        mask = cv2.inRange(hsv,tinggi,rendah)
        mask = cv2.medianBlur (mask,7)
        countours,_=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in countours:
            area= cv2.contourArea(cnt)

            if area >10 :
                x,y,w,h = cv2.boundingRect(cnt)
                cv2.rectangle(prame, (x,y), (x+w,y+h), (255,0,0),2)
                cv2.putText(prame, "WASPADA ROZAK DISEKITAR MU", (x,y -10),cv2.FONT_HERSHEY_COMPLEX, 0.7,(255,0,0),2)
        cv2.imshow("Utama", prame)
        cv2.imshow("Mask", mask)
        if cv2.waitKey(1)& 0xFF == ord ('q'):
            break
    Kam.release()
    cv2.destroyAllWindows()

if __name__=="__main__":
    Kam = cv2.VideoCapture(0)
    detectorColor(Kam)