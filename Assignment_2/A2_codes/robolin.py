import cv2
import numpy as np
import sys
img = cv2.imread(sys.argv[1])
#img = cv2.imread('tiles11.jpg')
# Converting images to grey scale for canny edge detection and hough transformation
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# Applying Gaussian blur before canny edge detection
blur = cv2.GaussianBlur(gray,(5,5),0)
# Applying canny edge detection to detect edges which will be later used to detect lines
edges = cv2.Canny(blur, 50, 150, apertureSize=3)
# Applying probabilistic hough trasnformation 
# minLineLength - Minimum length of line. Line segments shorter than this are rejected.
# maxLineGap - Maximum allowed gap between line segments to treat them as single line.
threshold = 90
minLineLength = 10
maxLineGap = 250
lines = cv2.HoughLinesP(edges, 1, np.pi/180,threshold, np.array([]),minLineLength, maxLineGap)
# Adding the lines detected in the original image
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
cv2.imwrite(('robolin-tiles3.jpg'),img)
#cv2.imshow('robolin-tiles3', img)
#cv2.waitKey(0)