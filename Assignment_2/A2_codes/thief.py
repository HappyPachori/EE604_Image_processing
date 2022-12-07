from math import gamma
import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys
img = cv2.imread(sys.argv[1],0)
gamma_correction = np.array(255*(img / 255) ** 0.5, dtype = 'uint8')
clahe = cv2.createCLAHE(clipLimit=5.0, tileGridSize=(5, 5))
equalized = clahe.apply(gamma_correction)
cv2.imwrite('enhanced-cctv3.jpg', equalized)
