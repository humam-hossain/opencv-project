import cv2 as cv

def rescaleFrame(frame, scale=0.75):
    # images, videos and live videos

    height = int(frame.shape[0] * scale)
    width = int(frame.shape[1] * scale)
    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # Live video
    capture.set(3, width)
    capture.set(4, height)
    
# reading image
# img = cv.imread("Photos/cat.jpg")
# img = rescaleFrame(img)
# cv.imshow("Cat", img)

# cv.waitKey(0)

# reading videos
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
