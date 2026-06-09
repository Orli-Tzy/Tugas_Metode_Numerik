# Soal 11.25 Orlicon_F5512510004

import numpy as np

def cholesky_decomposition(A):
    n = len(A)

    L = np.zeros((n, n))

    for i in range(n):

        for j in range(i + 1):

            if i == j:

                total = 0

                for k in range(j):
                    total += L[j, k] ** 2

                L[j, j] = np.sqrt(A[j, j] - total)

            else:

                total = 0

                for k in range(j):
                    total += L[i, k] * L[j, k]

                L[i, j] = (A[i, j] - total) / L[j, j]

    return L


# ==================================================
# DATA EXAMPLE 11.2
# ==================================================

A = np.array([
    [6, 15, 55],
    [15, 55, 225],
    [55, 225, 979]
], dtype=float)

L = cholesky_decomposition(A)

print("=" * 50)
print("SOAL 11.25 - CHOLESKY DECOMPOSITION")
print("UJI DENGAN EXAMPLE 11.2")
print("=" * 50)

print("\nMatriks L:")
print(np.round(L, 4))

print("\nVerifikasi L @ L.T:")
print(np.round(L @ L.T, 4))