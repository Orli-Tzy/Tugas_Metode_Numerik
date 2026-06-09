# Soal 11.2 Orlicon_F5512510004 

import numpy as np

A = np.array([
    [2.04,-1,0,0],
    [-1,2.04,-1,0],
    [0,-1,2.04,-1],
    [0,0,-1,2.04]
])

A_inv = np.linalg.inv(A)

print(A_inv)