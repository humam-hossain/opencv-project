import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

original = cv.imread("../photos/original.jpg")
sample = cv.imread("../photos/sample.jpg")

print(original.shape)
print(sample.shape)

diff = 255 - cv.absdiff(sample, original)

scale = 0.2

original_resized = rescaleFrame(original, scale)
sample_resized = rescaleFrame(sample, scale)
diff_resized = rescaleFrame(diff, scale)

cv.imshow("original", original_resized)
cv.imshow("sample", sample_resized)
cv.imshow("diff", diff_resized)

cv.waitKey(0)