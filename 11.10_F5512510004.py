# Soal 11.10 Orlicon_F5512510004

import numpy as np

A = np.array([
    [15,-3,-1],
    [-3,18,-6],
    [-4,-1,12]
])

b = np.array([
    3800,
    1200,
    2350
])

x = np.zeros(3)

es = 5

ea = np.ones(3)*100

iterasi = 0

while np.max(ea) > es:

    old = x.copy()

    x[0] = (3800 + 3*old[1] + old[2])/15

    x[1] = (1200 + 3*old[0] + 6*old[2])/18

    x[2] = (2350 + 4*old[0] + old[1])/12

    for i in range(3):

        if x[i] != 0:
            ea[i] = abs((x[i]-old[i])/x[i])*100

    iterasi += 1

print("Iterasi:",iterasi)
print("Konsentrasi:")
print(x)