import cv2
import numpy as np

list_warna = {
    "Merah":([0, 100, 100], [10, 255, 255]),
    "Hijau":([40, 100, 100], [80, 255, 255]),
    "Biru":([100, 100, 100], [130, 255, 255]),
    "Kuning":([20, 100, 100], [30, 255, 255]),
    "Ungu":([130, 100, 100],[150, 255, 255]),
    "Oranye":([10, 100, 100],[20, 255, 255])
}

def shapeandcolordetection(cam):
    while True:
        ret, frame = cam.read()
        if not ret: 
            print("Gagal membaca frame")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        for nama_warna,(lower,upper) in list_warna.items():
            mask = cv2.inRange(hsv, np.array(lower), np.array(upper))
            
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            
            for cnt in contours:
                area = cv2.contourArea(cnt) 

                if area < 500:
                    continue
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

                x, y, w, h = cv2.boundingRect(approx)
                
                sides = len(approx)
                shape = "Tidak diketahui"
                
                if sides == 3:
                    shape = "Segitiga"
                elif sides == 4:
                    shape = "Persegi"
                elif sides == 5:
                    shape = "Segilima"
                elif sides == 6:
                    shape = "Segienam"
                else:
                    shape = "Lingkaran / Oval"
                    
                cv2.rectangle(frame, (x,y), (x+w, y+h), (0, 255, 200), 2)
                label = f"{shape} - {nama_warna}"
                cv2.putText(frame, label, (x,y-10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255,255,255), 2)

        cv2.imshow("Frame",frame)
        cv2.imshow("Mask",mask)
        if cv2.waitKey(1) & 0xFF == ord('x'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Kamera tidak dapat dibuka")
    else:
        shapeandcolordetection(cam)

            

            