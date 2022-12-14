# opencv-project

## Getting started

```bash
$ pip install opencv-contrib-python caer
```

## Basics

### Reading images

```python
import cv2 as cv

img = cv.imread("img_source")
cv.imshow("window_name", img)

cv.waitKey(0)
```

### Reading videos

```python
import cv2 as cv

capture = cv.VideoCapture("video_src")

while True:
    isTrue, frame = capture.read()
    cv.imshow("Video", frame)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release() # releasing capture pointer
cv.destroyAllWindows()
```

### Drawing in image

```python
import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3), dtype="uint8")

cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,0,255), thickness=cv.FILLED)
cv.imshow("Rectangle", blank)

cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,255,0), thickness=cv.FILLED)
cv.imshow("Circle", blank)

cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (255,255,255), thickness=3)
cv.imshow("Line", blank)

cv.putText(blank, "Text", (0, 225), cv.FONT_HERSHEY_SIMPLEX, 1.0, (255, 0, 0), thickness=2)
cv.imshow("Text", blank)

cv.waitKey(0)
```

### Rescale frames

```python
import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

# rescale image
img = cv.imread("Photos/cat.jpg")
img = rescaleFrame(img)
cv.imshow("Cat", img)

cv.waitKey(0)

# rescale video
capture = cv.VideoCapture("Videos/dog.mp4")

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame)

    cv.imshow("Video", frame)
    cv.imshow("Video Resized", frame_resized)

    if cv.waitKey(20) & 0xFF==ord("d"):
        break

capture.release() # releasing capture pointer
cv.destroyAllWindows()
```

### Rescale live video

```python
def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)
```

### basic functions

```python
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
```

### Translate & rotate

```python
import cv2 as cv
import numpy as np


def translate(img, x, y):
    # x -> right 
    # -x -> left 
    # y -> down
    # -y -> up

    transMat = np.float32([[1,0,x],[0,1,y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(img, transMat, dimensions)

def rotate(img, angle, rotPoint=None):
    # angle > 0 -> anti-clockwise
    # angle < 0 -> clockwise
    (height, width) = img.shape[:2]

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

img = cv.imread("Photos/park.jpg")
cv.imshow("Park", img)

translated = translate(img, -100, -100)
cv.imshow("translated", translated)

rotated = rotate(img, 45)
cv.imshow("rotated", rotated)

# 0 -> vertical
# 1 -> horizontal
# -1 -> both

flip = cv.flip(img, 0)
cv.imshow("flip", flip)

cv.waitKey(0)
```

### Contours

```python
import cv2 as cv
import numpy as np

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cat", img)

blank = np.zeros(img.shape, dtype="uint8")
cv.imshow("blank", blank)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray", gray)

blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

canny = cv.Canny(blur, 125, 175)
cv.imshow("Canny", canny)

ret, thresh = cv.threshold(canny, 125, 255, cv.THRESH_BINARY)
cv.imshow("thresh", thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (255,255,255), 1)
cv.imshow("blank", blank)

cv.waitKey(0)
```

### Color spaces

```python
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
```

### Split & Merge Color Channels

```python
import cv2 as cv
import numpy as np

img = cv.imread("Photos/park.jpg")
cv.imshow("img", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# split image
b, g, r = cv.split(img)

blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow("Blue", blue)
cv.imshow("Green", green)
cv.imshow("Red", red)

print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# merge color channels
merged = cv.merge([b,g,r])
cv.imshow("Merged", merged)

cv.waitKey(0)
```

### Blurs

```python
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
```

### Bitwise operations

```python
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
```

### masking

```python
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
```

### Histogram

```python
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread("Photos/cats.jpg")
cv.imshow("Cats", img)

blank = np.zeros(img.shape[:2], dtype="uint8")

# grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("gray", gray)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow("Masked", mask)

# grayscale histogram
gray_hist = cv.calcHist([gray], [0], mask, [256], [0, 256])

plt.figure()
plt.title("Grayscale Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Color histrogram
circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 100, 255, -1)
mask = cv.bitwise_and(img, img, mask=circle)

colors = ('b', 'g', 'r')

plt.figure()
plt.title("Color Histogram")
plt.xlabel("Bins")
plt.ylabel("# of pixels")

for i,col in enumerate(colors):
    hist = cv.calcHist([img], [i], circle, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()

cv.waitKey(0)
```

### Thresholding

```python
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
```