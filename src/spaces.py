import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("park", img)

# BGR to gray
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

# HSV format (Hue Saturation Value): based on how human conceive color
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV_FULL)
cv.imshow("hsv", hsv)

# LAB/ L*a*b
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow("lab", lab)

# BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow("rgb", rgb)

# gray to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR_FULL)
cv.imshow("hsv-->bgr", hsv_bgr)

cv.waitKey(0)