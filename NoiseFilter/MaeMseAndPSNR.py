import cv2
import math

image = cv2.imread("tesla.jpg", 0)  # orjinal resim okundu
filteredImage = cv2.imread("TeslaVar10k100.jpeg",0)  # filtrelenmiş resim okundu

imageWidth = image.shape[1]
imageHeight = image.shape[0]

MxN = imageHeight * imageWidth

k = 100
sigma = 10
Err = 0
MSE = 0
MAE = 0
PSNR = 0

xPos = 0
yPos = 0

while xPos < imageHeight:
    while yPos < imageHeight:
        I0 = image.item(yPos, xPos)  # resim matrisi oluşturuldu
        Iy = filteredImage.item(yPos,xPos)  #filrelenmiş resim matrisi
        Err = I0 - Iy    # Err fonksiyonu hesaplandı
        MAE += (abs(Err) / MxN)  # MAE hesaplandı
        MSE += (Err * Err / MxN) # MSE hesaplandı
        yPos += 1
    yPos = 0
    xPos += 1

PSNR = 10 * math.log10(255*255/MSE) #dB

print("k = ", k,",Sigma = ", sigma, ",MAE = ", MAE, ",MSE = ", MSE, ",PSNR = ", PSNR, "[dB]")
