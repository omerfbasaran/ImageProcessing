import cv2
import matplotlib.pyplot
import numpy as np
import matplotlib as plt

image = cv2.imread("tesla.jpg", 0)
window: int = 3  # 3x3 9x9 15x15
border = window // 2  # kenarlıklar w/2
reflect = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_CONSTANT, None, value=0)

imageWidth = reflect.shape[1]
imageHeight = reflect.shape[0]

xMatris = np.zeros((imageWidth, imageHeight))
yMatris = np.zeros((imageWidth, imageHeight))


laplacien = [[-1, -1, -1],
             [-1, 9, -1],
             [-1, -1, 1]]

xPos = border
yPos = border

blockxPos = 0
blockyPos = 0

count = 0
mask = 0
final = 0

while border <= xPos < (imageWidth - border):  # resim döngüleri
    while border <= yPos < (imageHeight - border):
        while blockxPos < 3:  # blok döngüleri
            blockyPos = 0
            while blockyPos < 3:
                mask = laplacien[blockxPos][blockyPos]
                if blockxPos == 0 and blockyPos == 0:
                    Io = reflect.item(yPos - 1, xPos - 1)
                if blockxPos == 1 and blockyPos == 0:
                    Io = reflect.item(yPos - 1, xPos)
                if blockxPos == 2 and blockyPos == 0:
                    Io = reflect.item(yPos - 1, xPos + 1)
                if blockxPos == 0 and blockyPos == 1:
                    Io = reflect.item(yPos, xPos - 1)
                if blockxPos == 1 and blockyPos == 1:
                    Io = reflect.item(yPos, xPos)
                if blockxPos == 2 and blockyPos == 1:
                    Io = reflect.item(yPos, xPos + 1)
                if blockxPos == 0 and blockyPos == 2:
                    Io = reflect.item(yPos + 1, xPos - 1)
                if blockxPos == 1 and blockyPos == 2:
                    Io = reflect.item(yPos + 1, xPos)
                if blockxPos == 2 and blockyPos == 2:
                    Io = reflect.item(yPos + 1, xPos + 1)
                final += Io * mask
                # print("final", final, "Io", Io, "mask", mask)
                # print("xPos :", xPos, "yPos :", yPos, "blockxPos :", blockxPos, "blockyPos :", blockyPos)
                blockyPos += 1
            blockxPos += 1
        blockyPos = 0
        blockxPos = 0
        finalll = round((final + 535) * 255 / (318 + 535))  #normalizasyon
        blurimage.itemset((yPos, xPos), finalll)   #90 derece için max 710 min -251
        yMatris[xPos, yPos] = finalll                 #45 derece için max 1275 min -624
        # print(final)                              #Laplasyen için max 318 min -535
        final = 0
        #break
        yPos += 1
    yPos = border
    xPos = xPos + 1

print("max : ", yMatris.max())
print("min : ", yMatris.min())

cv2.imshow("new", blurimage)
cv2.waitKey()
cv2.destroyAllWindows()
#cv2.imwrite("teslaSharp45.jpeg",blurimage)

#dst = cv2.calcHist(blurimage, [0], None, [256], [0, 256])

#matplotlib.pyplot.hist(blurimage.ravel())
#matplotlib.pyplot.show()
