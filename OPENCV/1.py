import cv2

def openImage():
    img = cv2.imread('/home/rozak/Documents/Belajar Github/OPENCV/ROjak.png')
    if img is None:
        print("EROR GAk ada Fotonya")
        return

    cv2.imshow('ROjak', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=="__main__":
    openImage()