# Soal 11.28 Orlicon_F5512510004

import numpy as np

def pentadiagonal_solver(A, b):
    
    # Penyelesaian sistem pentadiagonal
    # menggunakan eliminasi Gauss tanpa pivoting.

    A = A.astype(float).copy()
    b = b.astype(float).copy()

    n = len(b)

    # Forward Elimination
    for k in range(n - 1):

        pivot = A[k, k]

        for i in range(k + 1, min(n, k + 3)):

            factor = A[i, k] / pivot

            A[i, k:] = A[i, k:] - factor * A[k, k:]
            b[i] = b[i] - factor * b[k]

    # Back Substitution
    x = np.zeros(n)

    x[n - 1] = b[n - 1] / A[n - 1, n - 1]

    for i in range(n - 2, -1, -1):

        total = 0

        for j in range(i + 1, n):
            total += A[i, j] * x[j]

        x[i] = (b[i] - total) / A[i, i]

    return x


# ======================================
# DATA SOAL 11.28
# ======================================

A = np.array([
    [8, -2, -1, 0, 0],
    [-2, 9, -4, -1, 0],
    [-1, -3, 7, -1, -2],
    [0, -4, -2, 12, -5],
    [0, 0, -7, -3, 15]
], dtype=float)

b = np.array([
    5,
    2,
    0,
    1,
    5
], dtype=float)

x = pentadiagonal_solver(A, b)

print("=" * 50)
print("SOAL 11.28 - PENTADIAGONAL SYSTEM")
print("=" * 50)

for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.6f}")