import cv2;

def openImage():

    img = cv2.imread('images2.jpeg')

    if img is None:
        print("Error: could not open or find the image.")
        return
    
    cv2.imshow('Foto Kerumunan', img)
    
    cv2.waitKey(0) #untuk waktu lama tampilan / durasi muncul nya gambar

    cv2.destroyAllWindows()

if __name__ == "__main__":
    openImage()