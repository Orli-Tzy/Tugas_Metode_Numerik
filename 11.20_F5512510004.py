# Soal 11.20 Orlicon_F5512510004

import numpy as np

n = 6

H = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        H[i,j] = 1/(i+j+1)

x_true = np.array([
    4,
    2,
    7,
    10,
    3,
    5
],dtype=float)

b = H @ x_true

x = np.linalg.solve(H,b)

cond_num = np.linalg.cond(H,np.inf)

print("Condition Number:")
print(cond_num)

print("\nSolusi:")
print(x)

print("\nError:")
print(x-x_true)