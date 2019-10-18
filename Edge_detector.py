import cv2 as cv


def detect_edge(img):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite("gray.jpg", gray)

    median = cv.medianBlur(gray, 7)
    cv.imwrite("median.jpg", median)

    laplace = cv.Laplacian(median, cv.CV_8U, ksize=5)
    cv.imwrite("laplace.jpg", laplace)

    # thresh = cv.adaptiveThreshold(laplace, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 3, 2)
    ret, thresh = cv.threshold(laplace, 125, 255, cv.THRESH_BINARY)
    cv.imwrite("thresh.jpg", thresh)

    return cv.bitwise_not(thresh)
