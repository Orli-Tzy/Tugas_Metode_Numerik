# Soal 11.19 Orlicon_F5512510004

import numpy as np

n = 10

H = np.zeros((n,n))

for i in range(n):
    for j in range(n):
        H[i,j] = 1/(i+j+1)

b = np.sum(H,axis=1)

cond_num = np.linalg.cond(H,np.inf)

x = np.linalg.solve(H,b)

lost_digits = np.log10(cond_num)

print("Condition Number:")
print(cond_num)

print("\nPerkiraan digit hilang:")
print(lost_digits)

print("\nSolusi:")
print(x)