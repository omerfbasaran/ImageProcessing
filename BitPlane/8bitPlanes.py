import cv2
img=cv2.imread("graypcb.jpg",0)
bitplane0=cv2.imread("graypcb.jpg",0)
bitplane1=cv2.imread("graypcb.jpg",0)
bitplane2=cv2.imread("graypcb.jpg",0)
bitplane3=cv2.imread("graypcb.jpg",0)
bitplane4=cv2.imread("graypcb.jpg",0)
bitplane5=cv2.imread("graypcb.jpg",0)
bitplane6=cv2.imread("graypcb.jpg",0)
bitplane7=cv2.imread("graypcb.jpg",0)

imageWidth = img.shape[1]
imageHeight = img.shape[0]

xPos = 0
yPos = 0

bitPlanes=[bitplane0,bitplane1,bitplane2,bitplane3,bitplane4,bitplane5,bitplane6,bitplane7]

bits = [0,0,0,0,0,0,0,0]

while xPos < imageWidth:
    while yPos < imageHeight:
        piksel = img.item(yPos, xPos)
        bit = 0
        while bit < 8:
            if piksel % 2 == 0:
                bits[bit] = 0
            else:
                bits[bit] = 1
            piksel = piksel >> 1

            if bits[bit]==1:
                ydisp=255
            else:
                ydisp=bits[bit]

            bitPlanes[bit].itemset((yPos, xPos), ydisp)
            bit += 1
        yPos = yPos + 1

    yPos = 0
    xPos = xPos + 1

cv2.imwrite("plane0.jpg", bitPlanes[0])
cv2.imwrite("plane1.jpg", bitPlanes[1])
cv2.imwrite("plane2.jpg", bitPlanes[2])
cv2.imwrite("plane3.jpg", bitPlanes[3])
cv2.imwrite("plane4.jpg", bitPlanes[4])
cv2.imwrite("plane5.jpg", bitPlanes[5])
cv2.imwrite("plane6.jpg", bitPlanes[6])
cv2.imwrite("plane7.jpg", bitPlanes[7])
