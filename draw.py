import numpy as np
import cv2

img1=np.zeros((512,512,3), np.uint8)
#img1=cv2.imread('cover.jpg', 1)
#img1=cv2.line(img1,(10,10),(500,10),(255,0,0),1)
img1 = cv2.circle(img1,(447,63), 63, (0,0,255), -1)
cv2.imshow('win1', img1)
cv2.waitKey(0)
