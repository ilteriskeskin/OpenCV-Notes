import cv2

img = cv2.imread('opencv-python.png', 1)

cv2.imshow('image', img)
cv2.waitKey(0)
