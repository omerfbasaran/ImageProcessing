import cv2
import numpy as np
import cmath

image = cv2.imread("tesla.jpg", 0)

imageHeight = image.shape[0]
imageWidth = image.shape[1]


xMatris = np.zeros((imageWidth, imageHeight), dtype=np.complex128)
amplitudeMatris = np.zeros((imageWidth, imageHeight))
phaseMatris = np.zeros((imageWidth, imageHeight))

xPos = 0
yPos = 0

while xPos < imageHeight:
    while yPos < imageHeight:
        xMatris[xPos, yPos] = image.item(yPos, xPos)  # resim matrisi oluşturuldu
        yPos += 1
    yPos = 0
    xPos += 1

xMatris = np.fft.fft2(xMatris)

xPos = 0
yPos = 0

while xPos < imageWidth:
    while yPos < imageHeight:
        amplitudeMatris[xPos, yPos] = abs(xMatris[xPos, yPos])
        phaseMatris[xPos, yPos] = cmath.phase(xMatris[xPos, yPos])
        phaseMatris[xPos, yPos] = round(((phaseMatris[xPos, yPos] + 3.14 ) / 6.28) * 255)
        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

genlik = 20*np.log(amplitudeMatris)
genlik = genlik.astype(np.uint8)
phase = phaseMatris.astype(np.uint8)

cv2.imwrite("teslaMagnitude.jpeg", genlik)
cv2.imwrite("teslaPhase.jpeg", phase)
