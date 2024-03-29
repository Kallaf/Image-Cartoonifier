import cv2 as cv


def smooth(img, img_dir):
    width = img.shape[1]
    height = img.shape[0]
    dim = (200, 200)
    # resize image
    resized = cv.resize(img, dim, interpolation = cv.INTER_AREA)
    #smooth image
    smoothed = resized
    for _ in range(7):
        smoothed = cv.bilateralFilter(smoothed, 9, 9, 7)
    # resize back
    dim = (width, height)

    smoothed = cv.resize(smoothed, dim, interpolation = cv.INTER_AREA)
    cv.imwrite(img_dir + "smoothed.jpg", smoothed)

    return smoothed
