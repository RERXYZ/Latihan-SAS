import cv2;
import numpy as np

select_hsv = None

def mouseCallback(event, x, y, flags, param):
    global select_hsv, frame_hsv
    
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel = frame_hsv[y, x]

        h, s, v  = int(pixel[0]), int(pixel[1]), int(pixel[2])
        select_hsv = (h, s, v)

        print("Selected HSV:")
        print("H:", h, "S:", s, "V:", v)

        lower = np.array([max(h-10,0), max(s-40,0), max(v-40,0)])
        upper = np.array([min(h+10,180), min(s+50,255), min(v+50,255)])

        print("Lower HSV:", lower)
        print("Upper HSV:", upper)

def inspectHSV(cap):
    global frame_hsv

    cv2.namedWindow('Frame')
    cv2.setMouseCallback('Frame', mouseCallback)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        cv2.imshow('Frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cap = cv2.VideoCapture(1)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, 300)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 150)
    inspectHSV(cap)