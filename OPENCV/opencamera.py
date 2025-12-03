import cv2

def openCamera(cam):
    while True:
        _, frame = cam.read()
        cv2.imshow('Camera', frame)
        if cv2.waitKey(9)& 0xFF == ord('q'):
            break
    cam.release()
    cv2.destroyAllWindows()
        
if __name__=="__main__":
    cam = cv2.VideoCapture(0)
    openCamera(cam)