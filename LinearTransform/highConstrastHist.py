import cv2
import numpy as np
from matplotlib import pyplot as plt


img=cv2.imread("lowcontrast.jpg",0)
dst = cv2.calcHist(img, [0], None, [256], [0, 256])

plt.hist(img.ravel(), 256, [0, 256])
plt.title('Histogram for gray scale image')
plt.show()