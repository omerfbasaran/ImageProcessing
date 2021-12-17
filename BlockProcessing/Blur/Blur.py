import cv2

image = cv2.imread("tesla.jpg", 0)
window: int = 3  # 3x3 9x9 15x15
border = window // 2  # kenarlıklar w/2
reflect = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_REFLECT)
blurimage = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_REFLECT)

imageWidth = reflect.shape[1]
imageHeight = reflect.shape[0]

xPos = border
yPos = border

blockxPos = xPos - border
blockyPos = yPos - border

toplam = 0
avrg = 0
count=0

while border <= xPos < (imageWidth - border):  #   resim döngüleri
    while border <= yPos < (imageHeight - border):
        while (xPos - border) <= blockxPos <= (xPos + border):  # blok döngüleri
            blockyPos = yPos - border
            while (yPos - border) <= blockyPos <= (yPos + border):
                summ += reflect.item(blockyPos, blockxPos)
                blockyPos += 1

            blockxPos += 1
        blockyPos = yPos - border
        blockxPos = xPos - border
        avrg = toplam//(window * window)
        blurimage.itemset((yPos, xPos), avrg)
        summ = 0
        avrg=0
        yPos += 1
    yPos = border
    xPos = xPos + 1

cv2.imwrite("tesla3x3blur.jpeg", blurimage)
