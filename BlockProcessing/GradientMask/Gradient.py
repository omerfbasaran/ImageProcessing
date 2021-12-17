import cv2
import numpy as np

image = cv2.imread("chessboard.jpg", 0)
window: int = 3  # 3x3
border = 1  # kenarlıklar w//2
reflect = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_CONSTANT, None, value=0) # karanlık kenarlıklar

imageWidth = reflect.shape[1]
imageHeight = reflect.shape[0]

xMatris = np.zeros((imageWidth, imageHeight))
yMatris = np.zeros((imageWidth, imageHeight))

xPos = 0
yPos = 0

while xPos < imageHeight:
    while yPos < imageHeight:
        xMatris[xPos, yPos] = reflect.item(yPos, xPos)  # resim matrisi oluşturuldu
        yPos += 1
    yPos = 0
    xPos += 1

Gx = [[0, -1, 0],
      [0, 0, 0],
      [0, 1, 0]]

for i in range(0, imageWidth-2):
    for j in range(0, imageHeight-2):
        piks = xMatris[i:i+3, j:j+3]
        deger = (Gx*piks).sum()
        if abs(deger) < 128:  # matrisin elemanlarını yazdırıp böyle bir normalizasyona karar verdim
            deger = 0
        if abs(deger) >= 128:  # yüksek üretilen değerleri yazdım sadece
            deger = 255   # geri kalanı ufak tefek gürültülerdi
        yMatris[i+1, j+1] = deger


cv2.imwrite("chessGyAbs.jpeg",yMatris)

"""
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
                mask = sharpeningMatrix[blockyPos][blockxPos]
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
        finalll = round(final / 44730 * 255)
        blurimage.itemset((yPos, xPos), finalll)
        variance[xPos, yPos] = final
        # print(final)
        final = 0
        # break
        yPos += 1
    yPos = border
    xPos = xPos + 1

# print(np.argmax(variance)) #max varyans 1014
cv2.imshow("new", blurimage)
cv2.waitKey()
cv2.destroyAllWindows()
# cv2.imwrite("chessGy.jpeg",blurimage)
"""