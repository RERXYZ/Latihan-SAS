import cv2;

def openImage():

    img = cv2.imread('Apaaja.jpg')

    if img is None:
        print("Error: Could not open or find the image.")
        return

    cv2.imshow('foto', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    openImage()