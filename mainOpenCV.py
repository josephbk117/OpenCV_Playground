import cv2
import sys
import  colourManipulation
import numpy as np

argList = sys.argv

if len(argList) < 4 or len(argList) > 4:
    print("Three arguments need to be passed")
    print("args :: = Input Image Location, Output Image Location, Edge Detection Operation")
else:
    img = cv2.imread(argList[1])
    cm = colourManipulation.ImageColourManip("add", img)
    resImg = cm.mulWithImage(img)
    cv2.imwrite('res/1x.jpg',resImg)
    print("Action to be performed : ",argList[3])
    if argList[3] == "laplace":
        laplacian = cv2.Laplacian(img, cv2.CV_64F)
        cv2.imwrite(argList[2],laplacian)
    elif argList[3] == "sobelx":
        sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)
        cv2.imwrite(argList[2], sobelx)
    elif argList[3] == "sobely":
        sobely = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)
        cv2.imwrite(argList[2], sobely)
    elif argList[3] == "canny":
        canny = cv2.Canny(img,150,150)
        cv2.imwrite(argList[2], canny)



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

