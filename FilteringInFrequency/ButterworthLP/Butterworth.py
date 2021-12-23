import numpy as np
import cv2
import math

image = cv2.imread("tesla.jpg", 0)
imageHeight = image.shape[0]
imageWidth = image.shape[1]

f = np.zeros((imageWidth, imageHeight))
h = np.zeros((imageWidth, imageHeight))

for i in range(imageWidth):
    for j in range(imageHeight):
        f[i, j] = ((-1) ** (i + j)) * image.item(i, j)

f = np.fft.fft2(f)

# H filtresi
d0 = 0.20 * imageWidth/2
n = 1 # derece

for i in range(imageWidth):
    for j in range(imageHeight):
        d = math.sqrt((i - imageWidth / 2) ** 2 + (j - imageHeight / 2) ** 2)
        h[i, j] = 1 / (1 + ((d / d0) ** (2 * n)))

f = np.fft.ifft2(f * h)

for i in range(imageWidth):
    for j in range(imageHeight):
        f[i, j] = ((-1) ** (i + j)) * f[i, j]

f = np.matrix.round(f.real)

cv2.imwrite("Butterworth020.jpeg", f)