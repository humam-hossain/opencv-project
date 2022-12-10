import cv2 as cv

img = cv.imread("Photos/cats.jpg")
cv.imshow("cats", img)

# Averaging blur
avg = cv.blur(img, (7,7))
cv.imshow("Average blur", avg)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7,7), 0)
cv.imshow("Gaussian blur", gauss)

# median blur
median = cv.medianBlur(img, 7)
cv.imshow("Median Blur", median)

# bilateral blur
bilateral = cv.bilateralFilter(img, 20, 70, 50)
cv.imshow("Bilateral Blur", bilateral)

cv.waitKey(0)