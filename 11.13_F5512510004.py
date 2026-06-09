# Soal 11.13 Orlicon_F5512510004

import numpy as np

lam = 1.2
es = 5

x = np.zeros(3)

ea = np.ones(3)*100

itr = 0

while np.max(ea) > es:

    old = x.copy()

    x1 = (-38 + 6*x[1] + x[2])/2

    x2 = (34 - 3*x1 + 7*x[2])

    x3 = (20 - 8*x1 + x2)/2

    x[0] = lam*x1 + (1-lam)*old[0]
    x[1] = lam*x2 + (1-lam)*old[1]
    x[2] = lam*x3 + (1-lam)*old[2]

    for i in range(3):
        if x[i] != 0:
            ea[i] = abs((x[i]-old[i])/x[i])*100

    itr += 1

print("Iterasi =", itr)
print(x)