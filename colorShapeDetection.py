import cv2
import numpy as np

def get_shape(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    sides = len(approx)

    if sides == 3:
        return "segitiga"
    elif sides == 4:
        return "persegi/persegi panjang"
    elif sides == 5:
        return "lima sisi"
    elif sides == 6:
        return "segienam"
    else:
        return "Tidak Tahu"
    # approx = cv2.approxPolyDP(contour, 0.02 * cv2.arcLength(contour, True), True)
    # sides = len(approx)
    
    # if sides == 3:
    #     return "triangle"
    # elif sides == 4:
    #     return "rect"
    # elif sides == 5:
    #     return "lima sisi"
    # elif sides > 5:
    #     return "lingkaran"
    # else:
    #     return "nggak tau"

def get_color(hsv, contour):
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    mean_hsv = cv2.mean(hsv, mask=mask)
    hue = mean_hsv[0]
    
    if hue < 10 or hue > 170:
        return "merah"
    elif 10 <= hue < 25:
        return "oren"
    elif 25 <= hue < 35:
        return "kuning"
    elif 35 <= hue < 85:
        return "ijo"
    elif 85 <= hue < 130:
        return "biru"
    elif 130 <= hue < 170:
        return "ungu"
    else:
        return "warna keren"

def openDetection(cam):
    while True:
        _, frame = cam.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        
        lower = np.array([0, 100, 100])
        upper = np.array([180, 255, 255])
        
        mask = cv2.inRange(hsv, lower, upper)
        mask = cv2.medianBlur(mask, 7)
        
        # peri = cv2.arcLength(contour, True)
        # blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        # approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
        # sides = len(approx)
        
        # if sides == 3:
        #     return "segitiga"
        # elif sides == 4:
        #     return "persegi/persegi panjang"
        # elif sides == 5:
        #     return "lima sisi"
        # else:
        #     return "lingkaran"

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area > 500:
                x, y, w, h = cv2.boundingRect(cnt)
                shape = get_shape(cnt)
                color = get_color(hsv, cnt)
                
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                text = f"{shape} {color}"
                cv2.putText(frame, text, (x, y-10), 
                            cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        
        cv2.imshow('Frame', frame)
        cv2.imshow('Mask', mask)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    openDetection(cam)
    pass