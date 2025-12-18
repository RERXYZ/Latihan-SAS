import cv2;
import numpy as np

def shapeDetector(cam):
    while True:
        _, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        blurred = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(blurred, 50, 150)
        _, thresh = cv2.threshold(blurred, 60, 255, cv2.THRESH_BINARY)

        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        for cnt in contours:
            area = cv2.contourArea(cnt)
            if area < 500:
                continue
            peri = cv2.arcLength(cnt, True)
            approx = cv2.approxPolyDP(cnt, 0.04 * peri, True)

            x, y, w, h = cv2.boundingRect(approx)
            sides = len(approx)
            shape = "Tidak Dikenal YNTKTS"
            if sides == 3:
                shape = "Segitiga"
            elif sides == 4:
                shape = "Persegi/Persegi Panjang"
            elif sides == 5:
                shape = "Lima Sisi"
            else:
                shape = "Lingkaran"
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(frame, shape, (x, y - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        cv2.imshow('Shape Detection', frame)
        cv2.imshow('Edges', edges)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()


    #         if area > 500:
    #             approx = cv2.approxPolyDP(cnt, 0.04 * cv2.arcLength(cnt, True), True)
    #             x, y, w, h = cv2.boundingRect(approx)

    #             if len(approx) == 3:
    #                 shape_name = "Triangle"
    #             elif len(approx) == 4:
    #                 shape_name = "Quadrilateral"
    #             elif len(approx) == 5:
    #                 shape_name = "Pentagon"
    #             else:
    #                 shape_name = "Circle"

    #             cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    #             cv2.putText(frame, shape_name, (x, y - 10),
    #                         cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    #     cv2.imshow('Shape Detection', frame)

    #     if cv2.waitKey(1) & 0xFF == ord('q'):
    #         break
    # cam.release()
    # cv2.destroyAllWindows()
if __name__ == "__main__":
    cam = cv2.VideoCapture(1)
    cam.set(cv2.CAP_PROP_FRAME_WIDTH, 600)
    cam.set(cv2.CAP_PROP_FRAME_HEIGHT, 300)
    shapeDetector(cam)