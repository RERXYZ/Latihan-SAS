import cv2

def detectShape(cam):
    while True:
        ret, frame = cam.read()
        if not ret:
            print("Gagal membaca frame")
            break

        frame = cv2.resize(frame, (640, 380))

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        for cnt in contours:
            area = cv2.contourArea(cnt)

            if area < 500:
                continue

            # Approx Poly untuk menghitung jumlah sisi
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

            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 200), 2)
            cv2.putText(frame, shape, (x, y - 10), cv2.FONT_ITALIC, 0.7, (0, 255, 200), 2)

        cv2.imshow("Frame", frame)
        cv2.imshow("Edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Kamera tidak dapat dibuka")
    else:
        detectShape(cam)