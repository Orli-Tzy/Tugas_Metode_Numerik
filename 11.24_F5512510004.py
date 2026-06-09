# Soal 11.24 Orlicon_F5512510004

import numpy as np

def thomas_algorithm(a, b, c, d):
   
    # Thomas Algorithm untuk sistem tridiagonal

    # a = subdiagonal (n-1)
    # b = diagonal utama (n)
    # c = superdiagonal (n-1)
    # d = ruas kanan (n)
    

    n = len(d)

    # Salin array agar data asli tidak berubah
    a = a.copy()
    b = b.copy()
    c = c.copy()
    d = d.copy()

    # Forward Elimination
    for i in range(1, n):
        factor = a[i-1] / b[i-1]

        b[i] = b[i] - factor * c[i-1]
        d[i] = d[i] - factor * d[i-1]

    # Back Substitution
    x = np.zeros(n)

    x[n-1] = d[n-1] / b[n-1]

    for i in range(n-2, -1, -1):
        x[i] = (d[i] - c[i] * x[i+1]) / b[i]

    return x


# =====================================================
# TEST PROGRAM DENGAN DATA EXAMPLE 11.1
# =====================================================

a = np.array([-1, -1, -1], dtype=float)

b = np.array([2.04, 2.04, 2.04, 2.04], dtype=float)

c = np.array([-1, -1, -1], dtype=float)

d = np.array([40.8, 0.8, 0.8, 200.8], dtype=float)

T = thomas_algorithm(a, b, c, d)

print("=" * 50)
print("SOAL 11.24 - THOMAS ALGORITHM")
print("UJI DENGAN EXAMPLE 11.1")
print("=" * 50)

for i in range(len(T)):
    print(f"T{i+1} = {T[i]:.3f}")