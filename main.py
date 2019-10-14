import cv2 as cv
import numpy as np
from Smoother import smooth
from Edge_detector import detect_edge

# Reading image
original = cv.imread('original.png')

# Image Processing
edge_detected =  detect_edge(original)
smoothed = smooth(original)
cartoonified = smoothed#cv.bitwise_and(edge_detected, smoothed)

# Show images
cv.imshow("Original",original)
cv.imshow("Cartoonified",cartoonified)
cv.waitKey(0)
cv.destroyAllWindows()