# Soal 11.1 Orlicon_F5512510004
# Thomas Algoritm dan Gauss Seidel

import numpy as np

A = np.array([
    [0.8, -0.4, 0],
    [-0.4, 0.8, -0.4],
    [0, -0.4, 0.8]
])

b = np.array([41, 25, 105])

x = np.linalg.solve(A, b)

print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])