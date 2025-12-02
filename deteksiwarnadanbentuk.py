import cv2
import numpy as np

def detectShapeAndColor(cam):
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Gagal membaca frame")
            break

        frame = cv2.resize(frame, (640, 380))

        # Convert ke HSV untuk deteksi warna
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Daftar batasan warna HSV
        boundaries = {
            "Merah": [(0, 100, 100), (10, 255, 255)],
            "Hijau": [(40, 70, 70), (80, 255, 255)],
            "Biru": [(100, 70, 70), (140, 255, 255)],
            "Kuning": [(20, 100, 100), (35, 255, 255)]
        }

        # Loop setiap warna
        for color_name, (lower, upper) in boundaries.items():

            lower = np.array(lower)
            upper = np.array(upper)

            mask = cv2.inRange(hsv, lower, upper)

            # Bersihkan noise
            mask = cv2.medianBlur(mask, 7)

            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area < 800:
                    continue

                # Deteksi bentuk dengan approxPolyDP
                peri = cv2.arcLength(cnt, True)
                approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

                x, y, w, h = cv2.boundingRect(approx)

                sides = len(approx)

                # Tentukan bentuk
                if sides == 3:
                    shape = "Segitiga"
                elif sides == 4:
                    shape = "Persegi"
                elif sides == 5:
                    shape = "Segilima"
                elif sides == 6:
                    shape = "Segienam"
                else:
                    shape = "Lingkaran"

                text = f"{color_name} {shape}"

                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 255), 2)
                cv2.putText(frame, text, (x, y - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)

        cv2.imshow("Deteksi Bentuk + Warna", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Kamera tidak dapat dibuka")
    else:
        detectShapeAndColor(cam)
