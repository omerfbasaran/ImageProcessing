import numpy as np

f = np.zeros((10, 10))
y = np.zeros((10, 10))
h = np.zeros((10, 10))
f[0:5, 0:5] = [[1, 3, 5, 7, 9],
               [2, 4, 6, 8, 10],
               [7, 8, 9, 10, 11],
               [1, 4, 8, 6, 3],
               [7, 5, 2, 9, 6]]

h[0:3, 0:3] = [[0, 1, 0],
               [1, 1, 1],
               [0, 1, 0]]

y = np.fft.ifft2(np.fft.fft2(f) * np.fft.fft2(h))
y = np.matrix.round(y.real)
print(y[0:5, 0:5])