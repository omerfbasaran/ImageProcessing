import cv2

image=cv2.imread("graypcb.jpg",0)

#   x1=0   # bu noktalar kullanılarak bulunan lineer denklem
#   x2=255  # y=40/255x+100 çıkar
#   y1=100
#   y2=140

imageWidth = image.shape[1]
imageHeight = image.shape[0]

xPos = 0
yPos = 0

while xPos < imageWidth:
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)  # pikselin değeri okundu
        ydisp=(40/255)*piksel+100
        image.itemset((yPos,xPos),ydisp)  # pikselin yeni değeri üzerine yazıldı

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("LowContrastPcb.jpg", image) #işlenmiş resmi kaydet