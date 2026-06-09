# Soal 11.23 Orlicon_F5512510004

import numpy as np
import matplotlib.pyplot as plt

n = np.arange(2, 21)

# Aproksimasi operasi Gaussian Elimination
gauss_ops = (2/3) * n**3

# Aproksimasi operasi Thomas Algorithm
thomas_ops = 8 * n

plt.plot(n, gauss_ops, marker='o', label='Gaussian Elimination')
plt.plot(n, thomas_ops, marker='s', label='Thomas Algorithm')

plt.xlabel('Ukuran Matriks (n)')
plt.ylabel('Jumlah Operasi')
plt.title('Perbandingan Operasi')
plt.legend()
plt.grid(True)

plt.show()