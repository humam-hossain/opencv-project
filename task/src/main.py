import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

original = cv.imread("../photos/tshirt_original.jpg")
sample1 = cv.imread("../photos/tshirt_sample_1.jpg")
sample2 = cv.imread("../photos/tshirt_sample_2.jpg")

original = cv.medianBlur(original, 13)
sample1 = cv.medianBlur(sample1, 13)
sample2 = cv.medianBlur(sample2, 13)

sample1_diff = cv.subtract(sample1, original)
sample2_diff = cv.subtract(sample2, original)

original_show = rescaleFrame(original, 0.1)
sample1_show = rescaleFrame(sample1_diff, 0.1)
sample2_show = rescaleFrame(sample2_diff, 0.1)

cv.imshow("original tshirt", original_show)
cv.imshow("sample1 tshirt", sample1_show)
cv.imshow("sample2 tshirt", sample2_show)

cv.waitKey(0)