# Soal 11.5 Orlicon_F5512510004

import numpy as np

A = np.array([
    [6,15,55],
    [15,55,225],
    [55,225,979]
],dtype=float)

b = np.array([
    152.6,
    585.6,
    2488.8
])

L = np.linalg.cholesky(A)

y = np.linalg.solve(L,b)

x = np.linalg.solve(L.T,y)

print("L:")
print(L)

print("\nKoefisien:")
print(x)