import cv2 as cv


def detect_edge(img, img_dir):
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    cv.imwrite(img_dir + "gray.jpg", gray)

    median = cv.medianBlur(gray, 7)
    cv.imwrite(img_dir + "median.jpg", median)

    laplace = cv.Laplacian(median, cv.CV_8U, ksize=5)
    cv.imwrite(img_dir + "laplace.jpg", laplace)

    ret, thresh = cv.threshold(laplace, 125, 255, cv.THRESH_BINARY)
    cv.imwrite(img_dir + "thresh.jpg", thresh)

    return cv.bitwise_not(thresh)
