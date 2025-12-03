import cv2
import numpy as jk

select_hsv= None

def mouseCallback(acara,x,y,flags,param):
    global select_hsv, frame_hsv

    if acara == cv2.EVENT_LBUTTONDOWN:
        pixell = frame_hsv[y,x]

        h,s,v= int(pixell[0]), int(pixell[1]), int(pixell[2]) 
        select_hsv =(h,s,v)

        print("\n=== Pixel Yang Terpilih===")
        print("Pixel 1 = ",h, "Pixel 2 =",s, "Pixel 3 = ",v)
        bawah = jk.array([max(h-10,0), max(s-40,0), max( v-40,0)])
        atas= jk.array([min (h +10, 180), min (s+40,255), min (v+40,255)])
        print ("Bawah: ", bawah)
        print ("Atas: ", atas)
def inspectHSV(cam):
    global frame_hsv

    cv2.namedWindow("Kamera")
    cv2.setMouseCallback("Kamera", mouseCallback)

    while True:
        ret, frame= cam.read()
        if not ret:
            print("Gak ada Kamera")
            break
        frame_hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        cv2.imshow ("Kamera", frame)
        if cv2.waitKey(1)& 0xFF == ord ('a'):
            break
    cam.release()
    cv2.destroyAllWindows()
if __name__=="__main__":
    cam = cv2.VideoCapture(0)
    inspectHSV(cam)
