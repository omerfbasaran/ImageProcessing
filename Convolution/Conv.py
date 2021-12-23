import numpy as np

f = np.zeros((9, 9))
y = np.zeros((9, 9)) # padding değerleri verildi
f[2:7, 2:7] = [[1, 3, 5, 7, 9],
               [2, 4, 6, 8, 10],
               [7, 8, 9, 10, 11],
               [1, 4, 8, 6, 3],
               [7, 5, 2, 9, 6]]

h = [[0, 1, 0],
     [1, 1, 1],
     [0, 1, 0]]

h = np.flipud(np.fliplr(h))  # h'yi tersle

for i in range(0, 7):
    for j in range(0, 7):
        fMatris = f[i:i + 3, j:j + 3]
        deger = (h * fMatris).sum()
        y[i, j] = deger

print(y[0:5, 0:5])
