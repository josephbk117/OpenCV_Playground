import cv2
import numpy as np
import matplotlib.pyplot as plt

#fourcc = cv2.VideoWriter_fourcc(*'XVID')
#out = cv2.VideoWriter('output.avi',fourcc,20.0,(640,480))

img = cv2.imread('res/cow.jpg',cv2.IMREAD_COLOR)
cv2.line(img,(0,0),(150,150),(255,0,0),15)
cv2.rectangle(img,(5,5),(35,35),(255,255,0),5)
cv2.circle(img,(15,15),25,(0,255,255),-1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

#plt.imshow(img,cmap = 'gray',interpolation = 'bicubic')
#plt.plot([50,100],[80,100],'c',linewidth = 5)
#plt.show()

#to save image out - cv2.imwrite('path',img)

#cap = cv2.VideoCapture(0)

#while True:
#      ret,frame = cap.read()
 #     gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
  #    out.write(frame)
   #   cv2.imshow('frame',frame)
    #  cv2.imshow('gray',gray)
     # if cv2.waitKey(1) & 0xFF == ord('q'):
      #      break

#cap.release()
#out.release()
#cv2.destroyAllWindows()
