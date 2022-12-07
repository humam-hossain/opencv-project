import cv2 as cv

img = cv.imread("Photos/park.jpg")
cv.imshow("Cat", img)

# grayscale image
grey = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grey", grey)

# gaussian blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

# canny edges
canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny Edges", canny)

# dilating image
dilated = cv.dilate(canny, (7,7), iterations=3)
cv.imshow("Dilated", dilated)

# eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
cv.imshow("Eroded", eroded)

# resize
resized = cv.resize(img, (1024,720), interpolation=cv.INTER_LINEAR)
cv.imshow("resized", resized)

# crop
cropped = img[200:300, 250:450]
cv.imshow("Cropped", cropped)

cv.waitKey(0)