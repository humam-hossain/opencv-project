import cv2 as cv
import numpy as np

blank = np.zeros((400,400), dtype="uint8")

rectangle = cv.rectangle(blank.copy(), (30,30), (370, 370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow("Rectangle", rectangle)
cv.imshow("Circle", circle)

# bitwise and
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow("Bitwise and", bitwise_and)

# bitwise or
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow("Bitwise or", bitwise_or)

# bitwise xor
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow("Bitwise xor", bitwise_xor)

# bitwise not
bitwise_rectangle_not = cv.bitwise_not(rectangle)
bitwise_circle_not = cv.bitwise_not(circle)

cv.imshow("Bitwise rectangle not", bitwise_rectangle_not)
cv.imshow("Bitwise circle not", bitwise_circle_not)

cv.waitKey(0)