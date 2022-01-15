import cv2
import numpy as np
import math
image = cv2.imread("tesla.jpg",0)

imageHeight = image.shape[1]
imageWidth = image.shape[0]
f = np.zeros((imageWidth, imageHeight))
y = np.zeros((imageWidth, imageHeight))
h = np.zeros((imageWidth, imageHeight))

x = np.linspace(0, 1, 512)
A = 30

for i in range(imageHeight):
    for j in range(imageWidth):
        f[i, j] = image.item(i, j)

for i in range(imageWidth):
    for j in range(imageHeight):
        f[i, j] = ((-1) ** (i + j)) * f[i, j]

noise = A * np.cos(2* np.pi * 20 * x)
y = f + noise
y = np.matrix.round(y)
y = np.fft.fft2(y)

d0 = 0.90 * imageWidth/2
n = 1 # derece

for i in range(imageWidth):
    for j in range(imageHeight):
        d = math.sqrt((i - imageWidth / 2) ** 2 + (j - imageHeight / 2) ** 2)
        h[i, j] = 1 / (1 + ((d / d0) ** (2 * n)))

y = np.fft.ifft2(y * h)
for i in range(imageWidth):
    for j in range(imageHeight):
        y[i, j] = ((-1) ** (i + j)) * y[i, j]

filtered = np.matrix.round(y.real)
cv2.imwrite("teslaFiltered.jpeg", filtered)

