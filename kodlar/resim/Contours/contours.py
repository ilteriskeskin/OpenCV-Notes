import cv2
import numpy as np

img = cv2.imread('opencv-python.png')

imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, thresh = cv2.threshold(imgray, 127, 255, 0)
img2, contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

contours1 = cv2.drawContours(img, contours, -1, (0,255,0), 3)

cv2.imshow('Contours', contours1)

cv2.waitKey(0)
cv2.destroyAllWindows()