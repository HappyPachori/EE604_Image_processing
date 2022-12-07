import numpy as np
import cv2
import sys
import math

def convert(im):
  x_array = np.array([[1, 0, 1.402], [1, -0.34414, -.71414], [1, 1.772, 0]])
  RGB = im.astype(np.float32)
  RGB[:,:,[1,2]] -= 128
  RGB = RGB.dot(x_array.T)
  RGB[RGB<0] = 0
  RGB[RGB>255] = 255
  return np.uint8(RGB)

Y = cv2.imread(sys.argv[1])
Cb = cv2.imread(sys.argv[2])
Cr = cv2.imread(sys.argv[3])

r_Cb = cv2.resize(Cb, (960,622))
r_Cr = cv2.resize(Cr,(960,622))
# print(Y.shape)
empty_array = np.empty((Y.shape[0], Y.shape[1], Y.shape[2]))

"""Adding channel images one by one"""
empty_array[:,:,0] = Y[:,:,0]
empty_array[:,:,2] = r_Cb[:,:,0]
empty_array[:,:,1] = r_Cr[:,:,0]

rgb = convert(empty_array)
cv2.imwrite(('flyingelephant.jpg'),rgb)


