import cv2
import numpy as np

def detectionShape(cam):
    while True:
        _, frame = cam.read()

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        blur = cv2.GaussianBlur(gray, (5, 5), 0)

        edges = cv2.Canny(blur, 50, 150)

        contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

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
            elif sides > 3 and sides <= 6:
                shape = "Polygon"  
            else:
                shape = "Lingkaran / Oval" 

            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)  # Blue Rectangle

            cv2.putText(frame, f"{shape} Detected", (x, y - 10), cv2.FONT_HERSHEY_COMPLEX, 0.7, (255, 0, 0), 2)

        cv2.imshow("Main", frame)
        cv2.imshow("Edges", edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("Error: Could not access the camera.")
    else:
        detectionShape(cam)