import cv2

image = cv2.imread("light.jpg",0) #resmi grayscale olarak oku

imageWidth = image.shape[1]
imageHeight = image.shape[0]

xPos = 0
yPos = 0
pikselsum=0

while xPos < imageWidth:
    while yPos < imageHeight:
        piksel = image.item(yPos, xPos)  # pikselin değeri okundu
        pikselsum=piksel+pikselsum  # pikselleri topladım
        yPos = yPos + 1
    yPos = 0
    xPos = xPos + 1

pikselavarage = pikselsum/(imageHeight*imageWidth)  # piksel ortalaması

xPos = 0
yPos = 0

while xPos < imageWidth:
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)  # pikselin değeri okundu
        if piksel <= pikselavarage:   #Eşik değeri 127 alındı ve büyük ise beyaza küçük ise siyaha eşitlendi
            piksel=0
        else:
            piksel=255
        image.itemset((yPos,xPos),piksel)  # pikselin yeni değeri üzerine yazıldı

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("lightTH2.jpg", image) #işlenmiş resmi kaydet