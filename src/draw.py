import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=cv.FILLED)
cv.imshow("Circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("Line", blank)

cv.putText(blank, "Hello, my name is Humam", (0, 225), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)