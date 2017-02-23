import cv2


class EdgeDetector:
    def __init__(self, image):
        self.image = image

    def laplacian(self):
        self.image = cv2.Laplacian(self.image, cv2.CV_64F)
        return self.image

    def sobel(self, xory, kernelSize=5):
        if xory == 'x':
            self.image = cv2.Sobel(self.image, cv2.CV_64F, 1, 0, ksize=kernelSize)
        else:
            self.image = cv2.Sobel(self.image, cv2.CV_64F, 0, 1, ksize=kernelSize)
        return self.image

    def canny(self, threshold1=100, threshold2=100):
        self.image = cv2.Canny(self.image, threshold1, threshold2)
        return self.image

    def saveImage(self, filepath):
        cv2.imwrite(filepath, self.image)

    def getImage(self):
        return self.image

    def displayWebcam(self,filter):
        cap = cv2.VideoCapture(0)
        while(True):
            _, frame = cap.read()
            img = cv2.Laplacian(frame,cv2.CV_64F)
            cv2.imshow('image result',img)
            k = cv2.waitKey(5) & 0xFF
            if k == 27:
                break
        cap.release()
        cv2.destroyAllWindows()