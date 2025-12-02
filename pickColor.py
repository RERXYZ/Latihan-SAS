import cv2
import numpy as np

selected_hsv = None

def mouseCallback(event, x, y, flags, param):

    global selected_hsv, frame_hsv

    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame_hsv[y, x]

        h, s, v = int(pixel[0]), int(pixel[1]), int(pixel[2])

        selected_hsv = (h, s, v)

        print("\n=== pixel yang terpilih ===")
        print("H = ", h, " S = ", s, " V = ", v)

        lower = np.array([max(h - 10, 0), max(s - 40, 0), max(v - 40, 0)])
        upper = np.array([min(h + 10, 100), min(s + 40, 255), min(v + 40, 255)])

        print("Lower : ", lower)
        print("Upper :", upper)

def inspectHSV(cam):

    global frame_hsv

    cv2.namedWindow("Kamera")
    cv2.setMouseCallback("Kamera", mouseCallback)

    while True:
        ret, frame = cam.read()
        if not ret:
            print("Gagal membaca kamera")

        frame = cv2.resize(frame, (640, 380))

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow("Kamera", frame)

        if cv2.waitKey(1) & 0xff == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows

if __name__ == "__main__":
    cam = cv2.VideoCapture(0)

    if not cam.isOpened():
        print("kamera tidak dapat di buka")
    else:
        inspectHSV(cam)
    