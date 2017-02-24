import numpy as np
import cv2
import sys

if len(sys.argv) <1:
	print 'Nedd one argument'
	exit
im=cv2.imread(sys.argv[ 1],1)
im_gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
mean=np.mean(im_gray)
#thresh=cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 5, 0)
ret, thresh=cv2.threshold(im_gray, mean-10, 255, 0)
cv2.imshow('threshold', thresh)
contours, hierarchy=cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

for contour in contours:
	rect=cv2.boundingRect(contour)
	if rect[ 2] * rect[ 3]>40000 and rect[ 2]*rect[ 3]<200000:
		cv2.drawContours(im, contour, -1, (0,255,0), 2)
		cv2.rectangle(im, (rect[ 0], rect[ 1]), (rect[ 0]+rect[ 2],rect[ 1]+rect[ 3]), (0,0,255), 2)

cv2.imshow('image', im)

cv2.waitKey(-1)
