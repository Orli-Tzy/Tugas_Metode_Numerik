# Soal 11.22 Orlicon_F5512510004

import numpy as np

A = np.array([
    [0, -7, 5],
    [0, 4, 7],
    [-4, 3, -7]
], dtype=float)

b = np.array([
    50,
    -30,
    40
], dtype=float)

x = np.linalg.solve(A, b)

print("Solusi:")
print("x1 =", x[0])
print("x2 =", x[1])
print("x3 =", x[2])

print("\nTranspose Matriks:")
print(A.T)

print("\nInverse Matriks:")
print(np.linalg.inv(A))