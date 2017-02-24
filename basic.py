import numpy as np
import cv2

img1=cv2.imread('cover.jpg', 1)
px=img1[ 100, 100]
print 'pixel at [ 100, 100] =', px
blue=img1[ 100, 100, 0]
print 'pixel at [ 100, 100, 0] =', blue
print img1.shape
print img1.size
print img1.dtype
title=img1[ 700:900, 200:400]
img1[ 0:200, 0:200]=title
b,g,r=cv2.split(img1)
cv2.imshow('win1', img1)
#cv2.imshow('win2', b)
#cv2.imshow('win3', g)
#cv2.imshow('win4', r)
img1[ :,:,2]=0
cv2.imshow('win5', img1)
cv2.waitKey(0)
