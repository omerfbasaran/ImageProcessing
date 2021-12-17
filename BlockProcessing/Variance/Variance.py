import cv2
#import numpy as np
image = cv2.imread("../Blur/tesla.jpg", 0)
image2 = image
window: int = 15  # 3x3 9x9 15x15
border = window // 2  # kenarlıklar w/2
reflect = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_REFLECT)
blurimage = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_REFLECT)

imageWidth = reflect.shape[1]
imageHeight = reflect.shape[0]

#variance=np.zeros((imageWidth ,imageHeight))

xPos = border
yPos = border


blockxPos = xPos - border
blockyPos = yPos - border

toplam = 0
avrg = 0
count = 0

while border <= xPos < (imageWidth - border):
    while border <= yPos < (imageHeight - border):
        while (xPos - border) <= blockxPos <= (xPos + border):
            blockyPos = yPos - border
            while (yPos - border) <= blockyPos <= (yPos + border):
                piksel = reflect.item(blockyPos, blockxPos)
                toplam += piksel

                blockyPos += 1

            blockxPos += 1
        blockyPos = yPos - border
        blockxPos = xPos - border
        avrg = toplam // (window * window)
        var = ((piksel - avrg) ** 2)/(window * window - 1)  #önce varyans matrisi oluşturup max aldım 1014 buldum
        variance = round(var/1014*255)           # Buna göre değerleri normalize ettim
        blurimage.itemset((yPos, xPos), variance)

        #variance[yPos,xPos]=var
        toplam = 0
        avrg = 0
        yPos += 1
    yPos = border
    xPos = xPos + 1
#print(np.argmax(variance)) #max varyans 1014
cv2.imwrite("tesla15x15var.jpeg", blurimage)
