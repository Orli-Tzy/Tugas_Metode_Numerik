# Soal 11.27 Orlicon_F5512510004

import numpy as np
import matplotlib.pyplot as plt

# Parameter soal
D = 2
U = 1
k = 0.2
dx = 2

# Boundary conditions
c0 = 80
c5 = 20

# Matriks koefisien hasil finite difference
A = np.array([
    [-1.2,   0.625, 0,      0],
    [ 0.375,-1.2,   0.625,  0],
    [ 0,     0.375,-1.2,    0.625],
    [ 0,     0,     0.375, -1.2]
], dtype=float)

# Vektor ruas kanan
b = np.array([
    -0.375*c0,
    0,
    0,
    -0.625*c5
], dtype=float)

# Menyelesaikan sistem
c_internal = np.linalg.solve(A, b)

# Gabungkan boundary dan solusi internal
c = np.concatenate(([c0], c_internal, [c5]))

# Titik x
x = np.arange(0, 11, 2)

print("Konsentrasi pada setiap titik:")

for xi, ci in zip(x, c):
    print(f"x = {xi:2d}   c = {ci:.4f}")

# Plot
plt.plot(x, c, marker='o')

plt.title("Concentration vs Distance")
plt.xlabel("Distance (x)")
plt.ylabel("Concentration (c)")
plt.grid(True)

plt.show()