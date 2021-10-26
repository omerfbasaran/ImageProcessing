import cv2
image=cv2.imread("lowcontrast.jpg",0)

#   x1=20   # bu noktalar kullanılarak bulunan denklemler
#   x2=40   # 0'dan x1(20)'e y=0.5x
#   y1=10   # 20'den x2(40)'ye y=10.5x-200
#   y2=220  # 40'dan L-1(255)'e y=0.162x+213.488

imageWidth = image.shape[1]
imageHeight = image.shape[0]

xPos = 0
yPos = 0

while xPos < imageWidth:
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)  # pikselin değeri okundu
        if piksel<=20:
            ydisp=0.5*piksel
        elif piksel >20 and piksel<=40: # denklemlerde yerine konularak piksel değerleri değiştirildi
            ydisp=10.5*piksel-200
        elif piksel>40 :
            ydisp=0.162*piksel+213.488

        image.itemset((yPos,xPos),ydisp)  # pikselin yeni değeri üzerine yazıldı

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("HighContrast.jpg", image) #işlenmiş resmi kaydet





