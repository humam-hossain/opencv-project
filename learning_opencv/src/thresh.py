import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# simple threshholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow("Simple Thresholded", thresh)

threshold_inv, thresh_inv = cv.threshold(gray, 0, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
cv.imshow("Simple Thresholded", thresh_inv)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow("Adaptive Threshholding", adaptive_thresh)

cv.waitKey(0)