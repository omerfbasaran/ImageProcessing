import cv2
import numpy as np
import math

image = cv2.imread("tesla.jpg", 0)

imageWidth = image.shape[1]
imageHeight = image.shape[0]
imgMatris = np.zeros((imageHeight, imageWidth))  # resim matrisi
yMatris = np.zeros((imageHeight, imageWidth))   # sonuc matrisi
var = 20 * 20
stdSapma = math.sqrt(var)
xPos = 0
yPos = 0
k = 50
countr = 0
while xPos < imageHeight:
    while yPos < imageHeight:
        imgMatris[xPos, yPos] = image.item(yPos, xPos)  # resim matrisi oluşturuldu
        yPos += 1
    yPos = 0
    xPos += 1

xPos = 0
yPos = 0

while countr < k:
    N = stdSapma * np.random.randn(imageHeight, imageWidth)
    while xPos < imageHeight:
        while yPos < imageWidth:
            yMatris[xPos, yPos] += imgMatris[xPos, yPos] + N[xPos, yPos]   # k adet gürültü eklendi
            yPos += 1
        yPos = 0
        xPos += 1
    xPos = 0
    countr += 1

xPos = 0
yPos = 0

while xPos < imageHeight:
    while yPos < imageHeight:
        piksel = yMatris[xPos, yPos]//k   # Pixel-wise ortalama alınarak gürültü filtrelendi
        image.itemset((yPos, xPos), piksel)
        yPos += 1
    yPos = 0
    xPos += 1


cv2.imwrite("TeslaVar20k50.jpeg",image)

