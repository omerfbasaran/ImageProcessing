import cv2
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
image = cv2.imread("windows11.jpeg", 0)
obj = cv2.imread("object.jpeg", 0)

objectHeight = obj.shape[0]
objectWidth = obj.shape[1]
border = objectWidth // 2

paddingF = cv2.copyMakeBorder(image, border, border, border, border, cv2.BORDER_REFLECT)
imageHeight = paddingF.shape[0]
imageWidth = paddingF.shape[1]
print(imageWidth, imageHeight)
print(objectWidth, objectHeight)
f = np.zeros((imageHeight, imageWidth))
h = np.zeros((objectHeight, objectWidth))
y = np.zeros((imageHeight, imageWidth))

for i in range(imageHeight):
    for j in range(imageWidth):
        f[i, j] = paddingF.item(i, j)

for i in range(objectHeight):
    for j in range(objectWidth):
        h[i, j] = obj.item(i, j)

hAvrg = 0

for i in range(objectHeight):
    for j in range(objectWidth):
        hAvrg += h[i, j]

hAvrg = hAvrg / (objectWidth * objectHeight)
piks = 0
for i in range(0, imageHeight - 2*border):
    for j in range(0, imageWidth - 2*border):
        piks = f[i:i+objectHeight, j:j+objectWidth]
        fxy = piks.mean()
        fcor = (piks - fxy)
        hcor = (h - hAvrg)
        y[i+border, j+border] = (fcor * hcor).sum()

# create the figure

xx, yy = np.mgrid[0:y.shape[0], 0:y.shape[1]]
fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_surface(xx, yy, y, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
plt.show()