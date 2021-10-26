import cv2
import numpy as np
from matplotlib import pyplot as plt

    # Code for plot the histograms

img=cv2.imread("HighContrast.jpg",0)
a = np.array(img)
plt.hist(a, bins = 'auto')
plt.title("histogram")
plt.show()
