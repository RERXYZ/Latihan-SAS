import cv2;

def openImage(path):
    
    img = cv2.imread('ambafoto.jpeg')

    if img is None:
        print("Error: Could not open or find the image.")
        return
    
    cv2.imshow('Display window', img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    pass
    openImage('../ambafoto.jpeg')

