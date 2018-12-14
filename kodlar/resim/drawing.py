import numpy as np
import cv2

img = np.zeros((512,512,3), np.uint8)

# Mavi renkte çizgi
cv2.line(img, (0,0), (511,511), (255,0,0), 5)

# Mavi renkte kare
cv2.rectangle(img,(384,0), (510, 128), (255,0,0), 5)

# Kırmızı renkte içi dolu daire
cv2.circle(img, (447,63), 63, (0,0,255), -1) # -1 içini doldurmak için

# Mavi renkte içi dolu yarım elips
cv2.ellipse(img, (256,256), (100,50), 0, 0, 180, 255, -1)

font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img, 'OpenCV', (10,500), font, 1, (255,255,255), 4, cv2.LINE_AA)

cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
