import cv2
import numpy as np
from matplotlib import pyplot as plt

img=cv2.imread('cover.jpg', 1)
cv2.imshow('win1', img)
cv2.waitKey(0)
#plt.imshow(img);
#plt.xticks([ ]), plt.yticks([ ])
#plt.show()
