# Soal 11.7 Orlicon_F5512510004

import numpy as np

A = np.array([
    [9,0,0],
    [0,25,0],
    [0,0,4]
],dtype=float)

L = np.linalg.cholesky(A)

print("L:")
print(L)

print("\nL @ L.T:")
print(L @ L.T)