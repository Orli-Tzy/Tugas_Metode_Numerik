# Soal 11.4 Orlicon_F5512510004

import numpy as np

A = np.array([
    [6,15,55],
    [15,55,225],
    [55,225,979]
],dtype=float)

L = np.array([
    [2.4495,0,0],
    [6.1237,4.1833,0],
    [22.454,20.917,6.1101]
])

hasil = L @ L.T

print("L * L.T")
print(hasil)

print("\nA")
print(A)

print("\nError")
print(A-hasil)