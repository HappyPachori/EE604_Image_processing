import cv2
import numpy as np
import sys
img = cv2.imread(sys.argv[1],0)
kernel = np.ones((9, 9), np.uint8)
rgb = cv2.split(img)
planes = []
nplanes = []
for plane in rgb:
    img_dilated = cv2.dilate(img, kernel, iterations=1)
    Gaussian = cv2.GaussianBlur(img_dilated, (7, 7), 0)
    difference = 255 - cv2.absdiff(plane, Gaussian)
    img_w_norm = cv2.normalize(difference,None, alpha=0, beta=255, norm_type=cv2.NORM_MINMAX, dtype=cv2.CV_8UC1)
    planes.append(difference)
    nplanes.append(img_w_norm)
result = cv2.merge(planes)
nresult = cv2.merge(nplanes)
cv2.imwrite('cleaned-gutter.jpg', nresult)