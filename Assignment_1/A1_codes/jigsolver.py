import cv2
import numpy as np
import matplotlib.pyplot as plt
import sys

img = cv2.imread(sys.argv[1])

a = img[0:200,0:190]      ## Selecting a subjection

a = a[:, :, [1,0,2]]      ## changing color of that subjection

b = img[200:409,0:190]    ## Selecting a subjection

b = cv2.flip(b,0)         ## Flipping section b

c = img[150:330, 515:700] ## Selecting a subjection
c = cv2.flip(c,1)         ## Flipping section c


d = img[370:421, 370:797] ## Selecting a subjection
d = cv2.flip(d,0)         ## Flipping section d

## Adjusting postions to solve
img[0: 209, 0:190] = b
img[199:399, 0:190] = a
img[150:330, 515:700] = c
img[370:421, 370:797] = d

cv2.imwrite(('jigsolved.jpg'), img)
