import cv2
import numpy as np
import math

image = cv2.imread("chessGxAbs.jpeg", 0)
image2 = cv2.imread("chessGyAbs.jpeg", 0)

imageWidth = image.shape[1]
imageHeight = image.shape[0]

yMatris = np.zeros((imageHeight, imageWidth))   # sonuc matrisi


xPos = 0
yPos = 0

while xPos < imageHeight:
    while yPos < imageHeight:
        gxPiksel = image.item(yPos, xPos)
        gyPiksel = image2.item(yPos, xPos)
        graAbs = math.sqrt(gxPiksel ** 2 + gyPiksel ** 2)
        yMatris[xPos][yPos] = graAbs
        image2.itemset((yPos, xPos), graAbs)
        yPos += 1
    yPos = 0
    xPos += 1

cv2.imwrite("GradAbsNew.jpeg",image2)
