import cv2
import numpy as np

selected_hsv = None
frame_hsv = None

def mouseCallback(event, x, y, flags, param):
    global selected_hsv, frame_hsv
    if event == cv2.EVENT_LBUTTONDOWN:  
        pixel = frame_hsv[y, x]  
        h, s, v = int(pixel[0]), int(pixel[1]), int(pixel[2]) 
        selected_hsv = (h, s, v)

        print("\n== Pixel yang terpilih ===")
        print(f"H = {h}, S = {s}, V = {v}")

        lower = np.array([max(h - 10, 0), max(s - 40, 0), max(v - 40, 0)])  # Batas bawah untuk warna
        upper = np.array([min(h + 10, 180), min(s + 40, 255), min(v + 40, 255)])  # Batas atas untuk warna

        print("Lower : ", lower)
        print("Upper : ", upper)

def detect_shape(cnt):
    approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)  # Menyederhanakan kontur jadi polygon

    if len(approx) == 4:  # Kalau bentuknya ada 4 sisi, berarti persegi atau persegi panjang
        return "Persegi/Panjang"
    elif len(approx) > 4:  # Kalau lebih dari 4 sisi, itu bisa lingkaran
        return "Lingkaran"
    else:  # Kalau bentuknya gak jelas, ya itu bentuk lain
        return "Bentuk Lain"

def detectColor(cam):
    global frame_hsv

    cv2.namedWindow("Kamera")  
    cv2.setMouseCallback("Kamera", mouseCallback)  

    while True:
        ret, frame = cam.read()  
        if not ret:
            print("Gagal membaca frame") 
            break

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)  

        if selected_hsv:
            h, s, v = selected_hsv
    
            lower = np.array([max(h - 10, 0), max(s - 40, 0), max(v - 40, 0)])
            upper = np.array([min(h + 10, 180), min(s + 40, 255), min(v + 40, 255)])

            mask = cv2.inRange(frame_hsv, lower, upper)  # Buat mask berdasarkan rentang warna yang kita pilih
            mask = cv2.medianBlur(mask, 5)  # Biar mask-nya lebih halus, ilangin noise

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)  # Cari kontur di mask

            for cnt in contours:
                area = cv2.contourArea(cnt)  # Hitung luas kontur
                if area > 500:  # Kalau luasnya cukup besar (nggak terlalu kecil), baru kita proses
                    x, y, w, h = cv2.boundingRect(cnt)  # Dapetin kotak pembatas dari kontur
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Gambarin kotak di sekitar objek

                    shape = detect_shape(cnt)  # Deteksi bentuk objeknya

                    if shape == "Lingkaran":
                        message = "Ini Lingkaran Bang!" 
                    elif shape == "Persegi/Panjang":
                        message = "Ini Persegi/Panjang Bang!"  
                    else:
                        message = f"Ini {shape}!"  

                    cv2.putText(frame, message, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)  

                    color = f"Color (H: {selected_hsv[0]}, S: {selected_hsv[1]}, V: {selected_hsv[2]})" 
                    print(f"\nDeteksi: {message} - {color}")

        cv2.imshow("Kamera", frame)  
        if cv2.waitKey(1) & 0xFF == ord('q'):  
            break

    cam.release()  
    cv2.destroyAllWindows() 

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)  # Ambil akses ke kamera (kamera utama)

    if not cam.isOpened():
        print("Kamera tidak dapat dibuka")  
    else:
        detectColor(cam) 