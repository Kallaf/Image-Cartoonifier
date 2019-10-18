import cv2 as cv
import numpy as np
from Smoother import smooth
from Edge_detector import detect_edge

# Reading image
original = cv.imread('original.png')

# Image Processing
thresh = detect_edge(original)
cv.imwrite("thresh2.jpg", thresh)

smoothed = smooth(original)
cv.imwrite("smoothed.jpg", smoothed)

thresh = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
cartoon = cv.bitwise_and(smoothed, thresh)
cv.imwrite("cartoon.jpg", cartoon)
