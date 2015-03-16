import numpy as np
import cv2

capture = cv2.VideoCapture(0)

while(True):

    sizeOfGaussian = 1

    # get one frame (image) from camera
    ret, frame = capture.read()

    # convert color image to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # resize, comment out if not wanted
    gray = cv2.resize(gray,(640,360))

    # apply Gaussian averaging
    gaussian = cv2.GaussianBlur(gray, (sizeOfGaussian,sizeOfGaussian), 0)

    # show result
    cv2.imshow('Gaussian averaging', gaussian)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# cleanup
capture.release()
cv2.destroyAllWindows()
