import sys

import cv2
import edgeDetection

# TODO: add video capability

argList = sys.argv

if len(argList) < 4 or len(argList) > 4:
    print("Three arguments need to be passed")
    print("args :: = Input Image Location, Output Image Location, Edge Detection Operation")
else:
    img = cv2.imread(argList[1])
    edg = edgeDetection.EdgeDetector(img)

    # cm = colourManipulation.ImageColourManip(img)
    # resImg = cm.blackAndWhite()
    # cv2.imwrite('res/1x.jpg',resImg)

    print("Action to be performed : ", argList[3])
    if argList[3] == "laplace":
        laplacian = edg.laplacian()

    elif argList[3] == "sobelx":
        sobelx = edg.sobel("x", 5)

    elif argList[3] == "sobely":
        sobely = edg.sobel("y", 5)

    elif argList[3] == "canny":
        canny = edg.canny(100, 100)
    edg.saveImage(argList[2])

'''

while (True):

    _, frame = cap.read()

    laplacian = cv2.Laplacian(frame,cv2.CV_64F)
    sobelx = cv2.Sobel(frame,cv2.CV_64F,1,0,ksize=5)
    sobely = cv2.Sobel(frame, cv2.CV_64F, 0, 1, ksize=5)
    edges = cv2.Canny(frame,100,100)

    cv2.imshow('original',frame)
    cv2.imshow('laplace',laplacian)
    cv2.imshow('sobel x', sobelx)
    cv2.imshow('sobel y', sobely)
    cv2.imshow('canny edges', edges)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()'''
