import cv2
import numpy as jk

bawah = None
atas = None
kerangka_hsv = None
def mouseCallBack(event, x, y, flags, param):
    global bawah, atas, kerangka_hsv
    if event == cv2.EVENT_LBUTTONDOWN:
        poxel = kerangka_hsv[y,x]
        h, s, v = int(poxel[0]), int(poxel[1]), int(poxel[2])
        print("\n Warna Yang Terpilih")
        print("Hue:  ", [h], "Saturasi: ", [s], "Value: ", [v])
        bawah = jk.array ([max (h- 20,0), max(s-50,50), max(v-50,50)])
        atas = jk.array ([min (h+ 20,179), min (s+50,255), min(v+50,255)])

        print("Batas bawah = ", bawah)
        print("Batas Atas = ", atas)

def pickColor(kamera):
    global kerangka_hsv
    cv2.namedWindow ("Pilih Warna")
    cv2.setMouseCallback("Pilih Warna",mouseCallBack)

    while True:
        ret, kerangka = kamera.read()
        if not ret:
            print("MANA KAMERANYA WOIIII")
            return
        kerangka_hsv=cv2.cvtColor(kerangka,cv2.COLOR_BGR2HSV)
        cv2.imshow("Pilih Warna", kerangka)
        if cv2.waitKey(1)&0xFF == ord('l'):
            break

    cv2.destroyWindow("Pilih Warna")
def detectColorShape(kamera):
    global bawah,atas
    if bawah is None or atas is None:
        print("PILIH WARNA YANG BENER DONGG")
        return
    while True:
        ret, kerangka = kamera.read()
        if not ret:
            print("GAK ADA KAMERANYA WOIIIII")
            break
        hsv =cv2.cvtColor (kerangka, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, bawah,atas)
        mask = cv2.medianBlur(mask, 7)

        contours, _=cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area<500:
                continue
            p = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt, 0.02 * p ,True)
            x,y,w,h = cv2.boundingRect(approx)
            sisi =len(approx)
            bentuk = "Unkown"
            if sisi == 3:
                bentuk = "Segitiga"
            elif sisi == 4:
                bentuk = "Persegi"
            elif sisi == 5:
                bentuk = "Segilima"
            elif sisi == 6:
                bentuk = "Segienam"
            else:
                bentuk = "Lingkaran"
            mask_roi= mask[y:y+h, x:x+w]
            kerangka_roi= kerangka[y:y+h,x:x+w]
            mean_color = cv2.mean(kerangka_roi, mask=mask_roi)
            b,g,r = int (mean_color[0]), int (mean_color[1]), int(mean_color[2])
            warna = "Unknown"
            if r > 150 and g < 100 and b < 100:
                warna = "Merah"
            elif g > 150 and r < 100 and b < 100:
                warna = "Hijau"
            elif b > 150 and r < 100 and g < 100:
                warna = "Biru"
            elif r > 150 and g > 150 and b < 100:
                warna = "Kuning"
            elif r > 150 and g > 150 and b > 150:
                warna = "Putih"
            elif r < 50 and g < 50 and b < 50:
                warna = "Hitam"
            else:
                warna = "Campuran"
            cv2.rectangle(kerangka, (x, y), (x + w, y + h),(b,g,r),2)
            cv2.putText(kerangka, f"{warna} {bentuk}", (x, y - 10),cv2.FONT_ITALIC,0.7, (b,g,r), 2)
            cv2.imshow("Deteksi Warna + Bentuk", kerangka)
            cv2.imshow("Mask ", mask)
            if cv2.waitKey(1) & 0xFF== ord ('q'):
                break
    kamera.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    kamera = cv2.VideoCapture(0)
    pickColor(kamera)
    detectColorShape(kamera)
