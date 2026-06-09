# Soal 11.18 Orlicon_F5512510004

import numpy as np

A = np.array([
    [4,3,2],
    [1,3,1],
    [2,1,3]
],dtype=float)

b = np.array([960,510,610],dtype=float)

x = np.linalg.solve(A,b)

print("Transistor =",x[0])
print("Resistor   =",x[1])
print("Chip       =",x[2])