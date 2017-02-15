import cv2


class ImageColourManip:
    def __init__(self, image):
        self.image = image

    def addToImage(self, img2):
        self.image = self.image + img2
        return self.image

    def subFromImage(self, img2):
        self.image = self.image - img2
        return self.image

    def mulWithImage(self, img2):
        self.image = self.image * img2
        return self.image

    def divWithImage(self, img2):
        self.image = self.image / img2
        return self.image

    def blackAndWhite(self):
        self.image = cv2.cvtColor(self.image, cv2.COLOR_BGR2GRAY)
        return self.image

    def saveImage(self, filepath):
        cv2.imwrite(filepath, self.image)

    def getImage(self):
        return self.image
