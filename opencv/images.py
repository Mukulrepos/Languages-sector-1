import cv2
import numpy as np

# how to read image
img=cv2.imread("opencv/j.jpeg")
# print(gray.shape)
# gray=cv2.cvtColor(img,cv2.rgb)
# print(gray.shape)

img[:,:,2]=0

cv2.imshow("window",img)
cv2.waitKey(0)