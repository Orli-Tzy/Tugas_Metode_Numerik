# Soal 11.17 Orlicon_F5512510004

import numpy as np
from scipy.optimize import fsolve

def F(v):
    x,y = v

    f = 4 - y - 2*(x**2)
    g = 8 - y**2 - 4*x

    return [f,g]

guess1 = [1,1]
guess2 = [-2,4]

sol1 = fsolve(F,guess1)
sol2 = fsolve(F,guess2)

print("Solusi 1:")
print(sol1)

print("\nSolusi 2:")
print(sol2)