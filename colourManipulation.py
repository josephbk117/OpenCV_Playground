import cv2
class ImageColourManip:
    def __init__(self,process,image):
        self.process = process
        self.image = image
    def addToImage(self,img2):
        return self.image + img2
    def subFromImage(self,img2):
        return self.image - img2
    def mulWithImage(self,img2):
        return self.image * img2
    def divWithImage(self,img2):
        return self.image / img2