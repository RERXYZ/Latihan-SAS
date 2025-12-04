import cv2
import numpy as np

selected_color = None
frame = None


def pick_color(event, x, y, flags, param):
    global selected_color, frame
    if event == cv2.EVENT_LBUTTONDOWN and frame is not None:
       
        bgr_color = frame[y, x]
        
        hsv_color = cv2.cvtColor(np.uint8([[bgr_color]]), cv2.COLOR_BGR2HSV)
        selected_color = hsv_color[0][0]  
        print(f"Color Picked: HSV({selected_color})")  


def openDetection(cam):
    global selected_color, frame
    while True:
        ret, frame = cam.read()

        if not ret:
            print("Gagal membaca frame dari kamera.")
            break

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        
        if selected_color is not None:
          
            lower_color = np.array([selected_color[0] - 20, 50, 50]) 
            upper_color = np.array([selected_color[0] + 20, 255, 255])

            
            mask = cv2.inRange(hsv, lower_color, upper_color)

      
            mask = cv2.medianBlur(mask, 7)

    
            contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

            for cnt in contours:
                area = cv2.contourArea(cnt)
                if area > 500: 
                    x, y, w, h = cv2.boundingRect(cnt)
                 
                    shape = get_shape(cnt)
                    color = get_color(hsv, cnt)
                    cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)  
                    text = f"{shape} {color} Kedeteksi abangku"
                    cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 255, 0), 1)

       
        cv2.imshow('Layarnya abangku', frame)

       
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cam.release()
    cv2.destroyAllWindows()


def get_shape(contour):
    peri = cv2.arcLength(contour, True)
    approx = cv2.approxPolyDP(contour, 0.04 * peri, True)
    sides = len(approx)

    if sides == 3:
        return "Segitiga"
    elif sides == 4:
  
        x, y, w, h = cv2.boundingRect(approx)
        aspect_ratio = float(w) / h
        if 0.95 <= aspect_ratio <= 1.05:
            return "Persegi"
        else:
            return "Persegi Panjang"
    elif sides > 4:
        return "Lingkaran / oval"  
    else:
        return "Bentuk Tidak Diketahui"


def get_color(hsv, contour):
    mask = np.zeros(hsv.shape[:2], dtype=np.uint8)
    cv2.drawContours(mask, [contour], 0, 255, -1)
    mean_hsv = cv2.mean(hsv, mask=mask)
    hue = mean_hsv[0]
    
    
    if hue < 10 or hue > 170: 
        return "Magenta"
    elif 10 <= hue < 25: 
        return "Oren"
    elif 25 <= hue < 35:
        return "Kuning"
    elif 35 <= hue < 85:
        return "Hijau"
    elif 85 <= hue < 130:
        return "Biru"
    elif 130 <= hue < 170:
        return "Merah"
    else:
        return "Warna lain ini bang!"


def check_camera():
    cam = cv2.VideoCapture(0, cv2.CAP_V4L2)  
    if not cam.isOpened():
        print("Kamera tidak dapat dibuka!")
        return None
    return cam

if __name__ == "__main__":

    cam = check_camera()

    if cam is None:
        print("Gagal terhubung ke kamera bang!")
    else:
      
        cam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)  
        cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

   
        cv2.namedWindow('Layar abangku')
        cv2.setMouseCallback('Layarnya abangku', pick_color)

       
        openDetection(cam)