# Soal 11.26 Orlicon_F5512510004

import numpy as np

def gauss_seidel(A, b, es=0.01, max_iter=100):

    n = len(b)

    x = np.zeros(n)

    for itr in range(max_iter):

        x_old = x.copy()

        for i in range(n):

            sigma = 0

            for j in range(n):

                if j != i:
                    sigma += A[i][j] * x[j]

            x[i] = (b[i] - sigma) / A[i][i]

        ea = np.zeros(n)

        for i in range(n):

            if x[i] != 0:
                ea[i] = abs((x[i] - x_old[i]) / x[i]) * 100

        if np.max(ea) < es:
            break

    return x, itr + 1, ea


# ==================================================
# DATA EXAMPLE 11.3
# ==================================================

A = np.array([
    [3, -0.1, -0.2],
    [0.1, 7, -0.3],
    [0.3, -0.2, 10]
], dtype=float)

b = np.array([
    7.85,
    -19.3,
    71.4
], dtype=float)

x, iterasi, ea = gauss_seidel(A, b)

print("=" * 50)
print("SOAL 11.26 - GAUSS SEIDEL")
print("UJI DENGAN EXAMPLE 11.3")
print("=" * 50)

print("\nJumlah Iterasi =", iterasi)

print("\nSolusi:")

for i in range(len(x)):
    print(f"x{i+1} = {x[i]:.6f}")

print("\nError Aproksimasi Relatif (%):")

for i in range(len(ea)):
    print(f"ea{i+1} = {ea[i]:.6f}")