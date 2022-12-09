import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats 2.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")
cv.imshow("blank", blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2 + 45, img.shape[0]//2), 100, 255, -1)
cv.imshow("masked", circle)

masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow("Masked", masked)

cv.waitKey(0)