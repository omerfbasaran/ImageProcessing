import cv2
from matplotlib import pyplot as plt

image= cv2.imread('graypcb.jpg', 0)


imageWidth = image.shape[1]
imageHeight = image.shape[0]

xPos = 0
yPos = 0
gamma=0.3       #aydınlatmak için "0.3" karartmak için "2" kullandım

while xPos < imageWidth:
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)  # pikselin değeri okundu
        r = piksel / 255
        piksel=r**gamma  #gamma dönüşümü
        piksel=piksel*255  #0 ile 1 arasında olan değer 255 yani (L-1) ile çarpıldı 8 bite dönüştürüldü
       # image.itemset((yPos,xPos),piksel)  # pikselin yeni değeri üzerine yazıldı

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("Lighterpcb.jpg", image) #işlenmiş resmi kaydet
