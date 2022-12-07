import numpy as np
import cv2
import sys

Number=int(sys.argv[1])                                  

output = np.zeros((300, 500))    ##size of output image
   
w = 60                                          #gap bet digits
r = 25                                          #radius of circlr

pattern = {}                                    ##patterns used for specific numbers
pattern[0] = [[1,1,1],[1,0,1],[1,0,1],[1,0,1],[1,1,1]]              
pattern[1] = [[0,1,0],[0,1,0],[0,1,0],[0,1,0],[0,1,0]]
pattern[2] = [[1,1,1],[0,0,1],[1,1,1],[1,0,0],[1,1,1]]
pattern[3] = [[1,1,1],[0,0,1],[1,1,1],[0,0,1],[1,1,1]]
pattern[4] = [[1,0,1],[1,0,1],[1,1,1],[0,0,1],[0,0,1]]
pattern[5] = [[1,1,1],[1,0,0],[1,1,1],[0,0,1],[1,1,1]]
pattern[6] = [[1,1,1],[1,0,0],[1,1,1],[1,0,1],[1,1,1]]
pattern[7] = [[1,1,1],[0,0,1],[0,0,1],[0,0,1],[0,0,1]]
pattern[8] = [[1,1,1],[1,0,1],[1,1,1],[1,0,1],[1,1,1]]
pattern[9] = [[1,1,1],[1,0,1],[1,1,1],[0,0,1],[1,1,1]]

l = 50
num_1 = int(Number/10)
num_2 = Number%10
dig = pattern[num_1]
for i in range(5):
    for j in range(3):
        if dig[i][j]:
            output = cv2.circle(output, (l + 5 + 10*j + r + 2*r*j , 5 + 10*i + r + 2*r*i ) , r, 255, -1)        # x coordinate of our circle = l + 5 + 10*j + r + 2*r*j & y coordinate of our circle = 5 + 10*i + r + 2*r*i    

           
l = 210 + w
dig = pattern[num_2]
for i in range(5):
    for j in range(3):
        if dig[i][j]:
            output = cv2.circle(output, (l + 5 + 10*j + r + 2*r*j , 5 + 10*i + r + 2*r*i ) , r, 255, -1)        # x coordinate of our circle = l + 5 + 10*j + r + 2*r*j & y coordinate of our circle = 5 + 10*i + r + 2*r*i    


cv2.imwrite(('dotmatrix.jpg'), output)
