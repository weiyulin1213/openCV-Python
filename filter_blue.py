import numpy as np
import cv2 

cap=cv2.VideoCapture(0)

while(1):
	_, frame=cap.read()

	hsv=cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

	# define range of blue in HSV
	lower_blue=np.array([ 110,20,20])
	upper_blue=np.array([ 130,255,255])

	# threshold the HSV image to get only blue
	mask=cv2.inRange(hsv, lower_blue, upper_blue)

	# bitwise AND mask and original image
	res=cv2.bitwise_and(frame, frame, mask=mask)

	cv2.imshow('frame', frame)
	cv2.imshow('mask', mask)
	cv2.imshow('res', res)
	k=cv2.waitKey(5) & 0xff
	if k== ord('q'):
		break

cv2.destroyAllWindows()
