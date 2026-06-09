# Soal 11.12 Orlicon_F5512510004

import numpy as np

lam = 0.95
es = 5

x = np.zeros(3)

ea = np.ones(3)*100

itr = 0

while np.max(ea) > es:

    old = x.copy()

    x1 = (50 - x[1] - 12*x[2])/(-3)
    x2 = 6*x1 - x[2] - 3
    x2 = -x2
    x3 = 40 - 6*x1 - 9*x2

    x[0] = lam*x1 + (1-lam)*old[0]
    x[1] = lam*x2 + (1-lam)*old[1]
    x[2] = lam*x3 + (1-lam)*old[2]

    for i in range(3):
        if x[i] != 0:
            ea[i] = abs((x[i]-old[i])/x[i])*100

    itr += 1

print("Iterasi =", itr)
print(x)