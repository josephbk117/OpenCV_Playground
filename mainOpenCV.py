import sys
import cv2
import edgeDetection
import colourManipulation

# TODO: add video capability

argList = sys.argv

if len(argList) < 5 or len(argList) > 5:
    print("Four arguments need to be passed")
    print("args :: = Input Image Location, Output Image Location, Typeof Operation (colour manip/edge detection) , Operation name")
else:
    img = cv2.imread(argList[1])
    print("Action to be performed : ", argList[3] , " with " , argList[4])
    if argList[3] == "edge detection":
        edg = edgeDetection.EdgeDetector(img)
        if argList[4] == "laplace":
            edg.laplacian()

        elif argList[4] == "sobelx":
            edg.sobel("x", 5)

        elif argList[4] == "sobely":
            edg.sobel("y", 5)

        elif argList[4] == "canny":
            edg.canny(100, 100)
        edg.saveImage(argList[2])
    if argList[3] == "colour manip":
        col = colourManipulation.ImageColourManip(img)
        if argList[4] == "blacknwhite":
            col.blackAndWhite()
            print("Converted to Black And White")
        elif argList[4] == "add image":
            path = str(input("Input image path : "))
            img2 = cv2.imread(path)
            col.addToImage(img2)

        col.saveImage(argList[2])

