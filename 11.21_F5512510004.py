# Soal 11.21 Orlicon_F5512510004

import numpy as np

A = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
], dtype=float)

I = np.eye(A.shape[0])

Aug = np.hstack((A, I))

print("Matriks A:")
print(A)

print("\nMatriks Identitas:")
print(I)

print("\nMatriks Augmented [A|I]:")
print(Aug)