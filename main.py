import cv2 as cv
import numpy as np
from Smoother import smooth
from Edge_detector import detect_edge

img_dir = "images/turkish-man/"

# Reading image
original = cv.imread(img_dir + 'original.png')

# Image Processing
thresh = detect_edge(original, img_dir)
cv.imwrite(img_dir + "thresh2.jpg", thresh)

smoothed = smooth(original, img_dir)
cv.imwrite(img_dir + "smoothed.jpg", smoothed)

thresh = cv.cvtColor(thresh, cv.COLOR_GRAY2BGR)
cartoon = cv.bitwise_and(smoothed, thresh)
cv.imwrite(img_dir + "cartoon.jpg", cartoon)
