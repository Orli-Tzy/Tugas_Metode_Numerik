# Soal 11.8 Orlicon_F5512510004

import numpy as np

A = np.array([
    [0.8,-0.4,0],
    [-0.4,0.8,-0.4],
    [0,-0.4,0.8]
],dtype=float)

b = np.array([41,25,105],dtype=float)

x = np.zeros(3)

lam = 1.2
es = 5

ea = np.ones(3)*100

itr = 0

while np.max(ea) > es:

    x_old = x.copy()

    for i in range(3):

        sigma = 0

        for j in range(3):

            if j != i:
                sigma += A[i,j]*x[j]

        x_new = (b[i]-sigma)/A[i,i]

        x[i] = lam*x_new + (1-lam)*x[i]

    for i in range(3):

        if x[i] != 0:
            ea[i] = abs((x[i]-x_old[i])/x[i])*100

    itr += 1

print("Iterasi:",itr)
print("Solusi:")
print(x)