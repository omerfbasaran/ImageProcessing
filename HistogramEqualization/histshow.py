import cv2
from matplotlib import pyplot as plt

image=cv2.imread("lowContrastPcbAfter.jpg",0)

dst = cv2.calcHist(image, [0], None, [256], [0, 256])

plt.hist(image.ravel(), 256, [0, 256])
plt.title('Histogram for low contrast grayscale image after Equalization')
plt.show()