# Soal 11.11 Orlicon_F5512510004

import numpy as np

es = 5

x1 = 0
x2 = 0
x3 = 0

ea1 = ea2 = ea3 = 100

iterasi = 0

while max(ea1, ea2, ea3) > es:

    old1, old2, old3 = x1, x2, x3

    x1 = (27 - 2*x2 + x3)/10

    x2 = (61.5 - 3*x1 + 2*x3)/6

    x3 = (-21.5 - x1 - x2)/5

    if x1 != 0:
        ea1 = abs((x1-old1)/x1)*100

    if x2 != 0:
        ea2 = abs((x2-old2)/x2)*100

    if x3 != 0:
        ea3 = abs((x3-old3)/x3)*100

    iterasi += 1

print("Jumlah iterasi =", iterasi)
print("x1 =", x1)
print("x2 =", x2)
print("x3 =", x3)