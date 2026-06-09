# Soal 11.16 Orlicon_F5512510004

import numpy as np

print("===== SOAL 11.16(a) =====")

A = np.array([
    [1,4,9],
    [4,9,16],
    [9,16,25]
],dtype=float)

b = np.array([14,29,50],dtype=float)

x = np.linalg.solve(A,b)

Ainv = np.linalg.inv(A)

cond_num = np.linalg.norm(A,np.inf) * np.linalg.norm(Ainv,np.inf)

print("Solusi:")
print(x)

print("\nInverse:")
print(Ainv)

print("\nCondition Number:")
print(cond_num)


print("\n===== SOAL 11.16(b) =====")

A = np.array([
    [1,4,9,16],
    [4,9,16,25],
    [9,16,25,36],
    [16,25,36,49]
],dtype=float)

b = np.array([30,54,86,126],dtype=float)

x = np.linalg.solve(A,b)

Ainv = np.linalg.inv(A)

cond_num = np.linalg.norm(A,np.inf) * np.linalg.norm(Ainv,np.inf)

print("Solusi:")
print(x)

print("\nInverse:")
print(Ainv)

print("\nCondition Number:")
print(cond_num)