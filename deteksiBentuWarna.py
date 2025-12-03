import cv2
import numpy as np


def deteksi_bentuk_biru(frame):
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # Range biru
    lower1 = np.array([100, 150, 50])
    upper1 = np.array([140, 255, 255])
    mask = cv2.inRange(hsv, lower1, upper1)

    blur = cv2.medianBlur(mask, 7)

    contours, _ = cv2.findContours(blur, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)

        if area < 500:  
            continue

        peri = cv2.arcLength(cnt, True)
        approx = cv2.approxPolyDP(cnt, 0.02 * peri, True)

        x, y, w, h = cv2.boundingRect(cnt)
        ratio = w /float(h)
        sides = len(approx)

        if sides == 3:
            shape = "Segitiga biru"
        elif sides == 4:
            if 0.9 < ratio <1.1:
                shape = "Persegi Biru"
            else:
                shape = "Persegi Panjang biru"
        elif sides == 5:
            shape = "Segilima biru"
        else:
            shape = "Lingkaran biru"

        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
        cv2.putText(frame, shape, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)

    cv2.imshow("Mask + blur", blur)
    cv2.imshow("Hasil", frame)

def main():
    cam = cv2.VideoCapture(0)
    if not cam.isOpened():
        print("Kamera tidak dapat dibuka")
        return
    try:
        while True:
            ret, frame = cam.read()
            if not ret:2

            deteksi_bentuk_biru(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
    except Exception as e:
        print("Terjadi error", e)

    finally:
        cam.release()
        cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
