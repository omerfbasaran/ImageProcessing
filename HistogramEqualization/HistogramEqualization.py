import cv2
import numpy as np
import math

def cdf(hist,MxN,value):
    j=0
    Px=0
    while j<=value:
        Px+=hist[j]/MxN
        j+=1
    return Px

image=cv2.imread('LowContrastPcb.jpg',0)
imageWidth = image.shape[1]
imageHeight = image.shape[0]
MxN=imageHeight*imageWidth
xPos = 0
yPos = 0

hist=np.zeros(256)

while xPos < imageWidth:   #hist() oluşturuldu
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)
        hist[piksel]+=1
        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

xPos = 0
yPos = 0

while xPos < imageWidth:
    while yPos < imageHeight:
        piks = image.item(yPos, xPos)
        ydisp: int = math.floor(cdf(hist,MxN,piks)*255)   #cdf'ten hesaplanan değerler 255 ile çarpılıp işlendi
        image.itemset((yPos,xPos),ydisp)

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("lowContrastPcbAfter.jpg",image)
