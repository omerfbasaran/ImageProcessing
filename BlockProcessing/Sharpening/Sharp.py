import cv2
import numpy as np

image = cv2.imread("chessboard.jpg", 0)
border = 1
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

sharpeningMatrix = [[-1, -1, -1],
                    [-1, 9, -1],
                    [-1, -1, -1]]

for i in range(0, imageWidth-2):
    for j in range(0, imageHeight-2):
        piks = xMatris[i:i+3, j:j+3]
        deger = (sharpeningMatrix * piks).sum()
        final = round((deger + 535) * 255 / (318 + 535))  #normalizasyon
                                                        #90 derece için max 710 min -251
        yMatris[xPos, yPos] = final                     #45 derece için max 1275 min -624
                                                        #Laplasyen için max 318 min -535
        yMatris[i+1, j+1] = deger


cv2.imwrite("teslaSharp45.jpeg",yMatris)