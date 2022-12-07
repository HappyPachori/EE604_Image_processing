import cv2
import numpy as np
import math
import sys
image = cv2.imread(sys.argv[1])

gbdiff = 0
grbdiff = 0
n = image.shape[0]*image.shape[1]

for x in range(image.shape[0]):
  for y in range(image.shape[1]):
    b, g, r = image[x,y]
    gbdiff = gbdiff + abs(g - b)
    grbdiff = grbdiff + abs(2*g - r - b)


gb_mean = int(gbdiff/n)
grbdiff_mean = int(grbdiff/n)
# print(gb_mean)
# print(grbdiff_mean)

if (gb_mean in range(7,24) and grbdiff_mean in range(0,13)) :
  print(3)

elif (gb_mean in range(0,81) and grbdiff_mean in range(12,86)):
  print(2)

else:
  print(1)




