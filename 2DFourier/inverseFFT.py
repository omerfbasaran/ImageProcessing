import cv2
import numpy as np

image = cv2.imread("tesla.jpg", 0)

imageHeight = image.shape[0]
imageWidth = image.shape[1]

xMatris = np.zeros((imageWidth, imageHeight), dtype=np.complex128)
yMatris = np.zeros((imageWidth, imageHeight))

xPos = 0
yPos = 0

xMatris = np.fft.fft2(image)

while xPos < imageHeight:
    while yPos < imageHeight:
        xMatris[xPos, yPos] = ((-1) ** (xPos + yPos)) * xMatris[xPos, yPos]
        yPos += 1
    yPos = 0
    xPos += 1

yMatris = np.fft.ifft2(xMatris)
yMatris = yMatris.astype(np.uint8)

cv2.imwrite("teslaiFFT2.jpeg", yMatris)