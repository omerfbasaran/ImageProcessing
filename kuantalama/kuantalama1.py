import cv2
import math

image = cv2.imread("tiger.jpg",0) #resmi grayscale olarak oku

imageWidth = image.shape[1]
imageHeight = image.shape[0]

xPos = 0
yPos = 0
k: int=7    #bit sayısı
q: int=256/2**k  # Q kuantalama aralığı  (Vmax-Vmin)/2^k

while xPos < imageWidth:
    while yPos < imageHeight:

        piksel=image.item(yPos,xPos)  # pikselin değeri okundu
        piksel: int=math.floor((piksel/q))  #kuantalama işlemi
        piksel=q*piksel+q/2   #Ydisplay için 8 bite tekrar dönüştürüldü
        image.itemset((yPos,xPos),piksel)  #kuantalanmış piksellerle yeni resim oluşturuldu

        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("7bit.jpg", image) #işlenmiş resmi kaydet
