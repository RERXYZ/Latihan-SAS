import cv2
import numpy as np

object_data = []
current_display_frame = None

def get_shape_name(approx_poly):
    num_vertices = len(approx_poly)
    if num_vertices == 3:
        return "Segitiga"
    elif num_vertices == 4:
        return "Kotak"
    elif num_vertices > 4:
        return "Lingkaran"
    else:
        return "Bentuk Lain"


def get_cmy_color(bgr):
    B, G, R = bgr
    if G > R and G > B:
        return "Cyan"
    elif B > R and B > G:
        return "Cyan"
    elif R > G and B > G:
        return "Magenta"
    elif R > B and G > B:
        return "Yellow"
    elif R > 200 and G < 100 and B < 100:
        return "Yellow"
    elif G > 200 and R < 100 and B < 100:
        return "Cyan"
    elif B > 200 and R < 100 and G < 100:
        return "Cyan"
    return "Tidak Dikenal"


def process_image(image):
    global object_data

    h, w, _ = image.shape

    roi_start_x = w // 3
    roi_end_x = 2 * w // 3
    roi_start_y = h // 3
    roi_end_y = 2 * h // 3

    roi_image = image[roi_start_y:roi_end_y, roi_start_x:roi_end_x]

    if roi_image.size == 0:
        object_data = []
        return []

    candidate_objects = []
    MIN_AREA_THRESHOLD = 300
    POLYGON_TOLERANCE = 0.06

    gray = cv2.cvtColor(roi_image, cv2.COLOR_BGR2GRAY)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)

    thresh = cv2.adaptiveThreshold(blurred, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                                   cv2.THRESH_BINARY_INV, 11, 2)

    kernel = np.ones((5, 5), np.uint8)
    thresh = cv2.dilate(thresh, kernel, iterations=1)

    contours, _ = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:
        current_area = cv2.contourArea(c)
        if current_area < MIN_AREA_THRESHOLD:
            continue

        peri = cv2.arcLength(c, True)
        approx = cv2.approxPolyDP(c, POLYGON_TOLERANCE * peri, True)

        x_roi, y_roi, w_roi, h_roi = cv2.boundingRect(approx)
        shape_name = get_shape_name(approx)

        if shape_name in ["Segitiga", "Kotak", "Lingkaran"]:
            x_global = x_roi + roi_start_x
            y_global = y_roi + roi_start_y

            candidate_objects.append({
                "name": shape_name,
                "area": current_area,
                "box": (x_global, y_global, w_roi, h_roi),
                "contour": c + (roi_start_x, roi_start_y)
            })

    candidate_objects.sort(key=lambda obj: obj['area'], reverse=True)
    object_data = candidate_objects[:1]

    return object_data


def draw_objects(image, objects):
    img_with_boxes = image.copy()

    h, w, _ = img_with_boxes.shape
    roi_start_x = w // 3
    roi_end_x = 2 * w // 3
    roi_start_y = h // 3
    roi_end_y = 2 * h // 3

    cv2.rectangle(img_with_boxes, (roi_start_x, roi_start_y), (roi_end_x, roi_end_y), (255, 0, 0), 2)
    cv2.putText(img_with_boxes, "Tempat Deteksi", (roi_start_x, roi_start_y - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 1)

    for obj in objects:
        x, y, w, h = obj["box"]
        shape_name = obj["name"]
        color = (0, 255, 0)

        cv2.rectangle(img_with_boxes, (x, y), (x + w, y + h), color, 2)
        label = f"{shape_name}"

        text_y = y + h + 20
        cv2.putText(img_with_boxes, label, (x, text_y),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    return img_with_boxes


def mouse_callback(event, x, y, flags, param):
    global current_display_frame
    if event == cv2.EVENT_LBUTTONDOWN:
        print("\n--- KLIK DETECTED ---")
        if current_display_frame is None:
            print("Frame belum siap.")
            return

        bgr_color = current_display_frame[y, x]
        cmy_name = get_cmy_color(bgr_color)
        found_object = False

        for obj in object_data:
            if cv2.pointPolygonTest(obj["contour"], (x, y), False) >= 0:
                print("====================================")
                print(f"Bentuk di klik: **{obj['name']}**")
                print("**PRIORITAS: OBJEK INI YANG PALING DEKAT**")
                print(f"Warna Piksel (BGR): {bgr_color}")
                print(f"Warna **CMY** yang dilaporkan: **{cmy_name}**")
                print("====================================")
                found_object = True
                break

        if not found_object:
            print(f"Tidak ada objek yang terdeteksi di koordinat ({x}, {y}).")
            print(f"Warna Piksel (BGR): {bgr_color}")
            print(f"Warna **CMY** yang dilaporkan: **{cmy_name}**")


def main():
    global current_display_frame

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Tidak dapat membuka kamera. Pastikan kamera terhubung.")
        return

    window_name = "Shape Detector"
    cv2.namedWindow(window_name)
    cv2.setMouseCallback(window_name, mouse_callback)

    print(f"Program sekarang fokus pada ROI.")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Gagal menerima frame.")
            break

        detected_objects = process_image(frame)
        display_image = draw_objects(frame, detected_objects)
        current_display_frame = display_image

        cv2.imshow(window_name, display_image)

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()