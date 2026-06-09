# Tugas Bab 11 – Numerical Methods for Engineers

Nama : Orlicon Yaleswira Widodo  
NIM : F5512510004  
Kelas : Teknik Informatika A

Repository ini berisi penyelesaian Soal 11.1–11.28 menggunakan Python berdasarkan Bab 11 (*Special Matrices and Gauss-Seidel*) pada buku *Numerical Methods for Engineers*.

---

# Soal 11.1

## Deskripsi
Menyelesaikan sistem persamaan linear tridiagonal menggunakan metode matriks.

## Metode
- Membentuk matriks koefisien A.
- Membentuk vektor ruas kanan b.
- Menyelesaikan sistem menggunakan `numpy.linalg.solve()`.

## Output
- Nilai x₁
- Nilai x₂
- Nilai x₃

## Kesimpulan
Solusi sistem diperoleh dengan metode penyelesaian linear algebra dari NumPy.

---

# Soal 11.2

## Deskripsi
Menghitung invers matriks tridiagonal.

## Metode
- Membentuk matriks A.
- Menggunakan `numpy.linalg.inv()`.

## Output
- Matriks invers A⁻¹.

## Kesimpulan
Invers matriks berhasil dihitung menggunakan metode numerik bawaan NumPy.

---

# Soal 11.3

## Deskripsi
Menentukan distribusi temperatur pada sistem satu dimensi.

## Metode
- Membentuk sistem persamaan linear.
- Menyelesaikan sistem menggunakan `numpy.linalg.solve()`.

## Output
- Temperatur pada setiap node.

## Kesimpulan
Distribusi temperatur pada node-node sistem berhasil diperoleh.

---

# Soal 11.4

## Deskripsi
Memverifikasi hasil dekomposisi Cholesky dengan menghitung kembali matriks asal.

## Metode
- Mengalikan matriks L dengan transpose-nya.
- Membandingkan hasil dengan matriks A.

## Output
- Matriks hasil perkalian `L @ L.T`.
- Selisih terhadap matriks A.

## Kesimpulan
Jika hasil `L @ L.T` sama dengan A, maka dekomposisi Cholesky valid.

---

# Soal 11.5

## Deskripsi
Menentukan koefisien regresi kuadratik menggunakan sistem persamaan linear.

## Metode
- Membentuk matriks koefisien.
- Menyelesaikan sistem menggunakan `numpy.linalg.solve()`.
- Menghitung koefisien a₀, a₁, dan a₂.

## Output
- a₀
- a₁
- a₂

## Kesimpulan
Koefisien persamaan kuadratik berhasil diperoleh dari sistem linear yang dibentuk.

---

# Soal 11.6

## Deskripsi
Melakukan Cholesky Decomposition terhadap matriks simetris positif definit.

## Metode
- Menggunakan `numpy.linalg.cholesky()`.
- Memverifikasi bahwa A = LLᵀ.

## Output
- Matriks L.
- Hasil verifikasi `L @ L.T`.

## Kesimpulan
Diperoleh matriks segitiga bawah L sehingga A dapat direkonstruksi kembali dari LLᵀ.

---

# Soal 11.7

## Deskripsi
Melakukan Cholesky Decomposition pada matriks diagonal.

## Metode
- Menggunakan `numpy.linalg.cholesky()`.

## Output
- Matriks L.
- Verifikasi `L @ L.T`.

## Kesimpulan
Karena matriks diagonal positif definit, hasil L merupakan akar kuadrat dari elemen diagonal matriks A.

---

# Soal 11.8

## Deskripsi
Menyelesaikan sistem pada Soal 11.1 menggunakan metode Gauss-Seidel dengan relaksasi.

## Metode
- Iterasi Gauss-Seidel.
- Menggunakan faktor relaksasi λ = 1.2.
- Iterasi dilakukan sebanyak 50 langkah.

## Output
- Nilai x₁
- Nilai x₂
- Nilai x₃

## Kesimpulan
Metode Gauss-Seidel dengan overrelaxation digunakan untuk mempercepat konvergensi solusi.

---

# Soal 11.9

## Deskripsi
Menyelesaikan sistem konsentrasi reaktor menggunakan metode linear algebra.

## Metode
- Menyusun matriks koefisien.
- Menyelesaikan sistem menggunakan `numpy.linalg.solve()`.

## Output
- Nilai konsentrasi untuk masing-masing variabel.

## Kesimpulan
Konsentrasi komponen berhasil dihitung dari sistem persamaan linear.

---

# Soal 11.10

## Deskripsi
Menyelesaikan sistem yang sama dengan Soal 11.9 menggunakan iterasi Jacobi atau skema iteratif.

## Metode
- Iterasi dengan tebakan awal nol.
- Menggunakan parameter relaksasi ω = 1.1.

## Output
- Nilai konsentrasi hasil iterasi.

## Kesimpulan
Solusi dapat diperoleh secara iteratif dengan bantuan faktor relaksasi.

---

# Soal 11.11

## Deskripsi
Menyelesaikan sistem persamaan linear tiga variabel menggunakan metode Gauss-Seidel.

## Metode
- Menyusun bentuk iterasi dari sistem.
- Menghitung error relatif sampai memenuhi toleransi.

## Output
- Jumlah iterasi.
- Nilai x₁, x₂, dan x₃.

## Kesimpulan
Metode iteratif berhasil memberikan solusi sistem.

---

# Soal 11.12

## Deskripsi
Menyelesaikan sistem persamaan linear dengan relaksasi.

## Metode
- Menggunakan faktor relaksasi λ = 0.95.
- Menghitung solusi secara iteratif.

## Output
- Jumlah iterasi.
- Vektor solusi.

## Kesimpulan
Metode relaksasi digunakan untuk menjaga kestabilan iterasi.

---

# Soal 11.13

## Deskripsi
Menyelesaikan sistem persamaan linear tiga variabel dengan overrelaxation.

## Metode
- Menggunakan faktor relaksasi λ = 1.2.
- Iterasi dilakukan sampai galat relatif memenuhi kriteria.

## Output
- Jumlah iterasi.
- Vektor solusi.

## Kesimpulan
Overrelaxation digunakan untuk mempercepat proses konvergensi.

---

# Soal 11.14

## Deskripsi
Menganalisis pengaruh slope terhadap konvergensi metode Gauss-Seidel berdasarkan Gambar 11.5.

## Metode
Dilakukan analisis konseptual terhadap perilaku metode Gauss-Seidel ketika seluruh persamaan memiliki gradien (slope) yang sama, yaitu -1.

## Hasil
Apabila seluruh persamaan memiliki gradien -1, maka garis-garis yang terbentuk akan sejajar atau hampir sejajar. Dalam kondisi ini tidak terdapat titik perpotongan tunggal yang jelas sehingga solusi sistem menjadi sulit ditentukan secara unik.
Jika metode Gauss-Seidel diterapkan pada sistem seperti ini, proses iterasi cenderung tidak konvergen atau memerlukan sangat banyak iterasi untuk mendekati solusi. Hal ini terjadi karena setiap iterasi tidak mampu mengarahkan solusi menuju satu titik perpotongan yang stabil.
Oleh karena itu, jika metode Gauss-Seidel diterapkan pada sistem dengan seluruh gradien bernilai -1, metode tersebut cenderung mengalami konvergensi yang sangat lambat atau bahkan divergen. Kondisi ini menunjukkan bahwa karakteristik matriks koefisien sangat memengaruhi keberhasilan metode iteratif dalam menemukan solusi.

## Kesimpulan
Metode Gauss-Seidel tidak dijamin konvergen pada kondisi tersebut.

---

# Soal 11.15

## Deskripsi
Menentukan sistem persamaan yang tidak dapat diselesaikan dengan metode iteratif seperti Gauss-Seidel.

## Metode
Setiap sistem persamaan diperiksa berdasarkan syarat dominasi diagonal. Dominasi diagonal merupakan salah satu syarat penting agar metode iteratif seperti Gauss-Seidel dapat konvergen.

## Hasil
Keberhasilan metode Gauss-Seidel sangat dipengaruhi oleh sifat matriks koefisien, khususnya dominasi diagonal. Sebuah matriks dikatakan dominan diagonal apabila nilai absolut elemen diagonal pada setiap baris lebih besar daripada jumlah nilai absolut elemen-elemen lainnya pada baris yang sama. Kondisi ini membantu menjamin konvergensi metode iteratif.
Pada Set One, meskipun tidak seluruh baris memenuhi dominasi diagonal secara langsung, sistem masih dapat disusun ulang sehingga peluang konvergensinya menjadi lebih baik. Oleh karena itu, metode Gauss-Seidel masih dapat digunakan untuk menyelesaikan sistem tersebut. 
Pada Set Two, beberapa baris tidak memenuhi syarat dominasi diagonal dan tidak mudah diatur ulang untuk memperoleh dominasi diagonal yang kuat. Kondisi ini menyebabkan proses iterasi berpotensi tidak konvergen atau menghasilkan kesalahan yang besar.
Pada Set Three, dominasi diagonal juga tidak terpenuhi pada sebagian besar persamaan. Akibatnya, metode Gauss-Seidel tidak memiliki jaminan konvergensi dan dapat menghasilkan solusi yang tidak stabil.
Berdasarkan analisis tersebut, Set Two dan Set Three merupakan sistem yang paling berpotensi gagal diselesaikan menggunakan metode Gauss-Seidel, sedangkan Set One masih memiliki kemungkinan untuk konvergen setelah dilakukan pengaturan ulang persamaan. Dengan demikian, dominasi diagonal merupakan faktor penting yang harus diperhatikan sebelum menerapkan metode iteratif pada sistem persamaan linear.

## Kesimpulan
Set Two dan Set Three paling berpotensi tidak konvergen, sedangkan Set One masih memiliki kemungkinan untuk diselesaikan setelah penyusunan ulang persamaan.

---

# Soal 11.16

## Deskripsi
Menganalisis sensitivitas matriks menggunakan condition number.

## Metode
- Menghitung invers matriks.
- Menghitung condition number dengan norma baris.
- Menyelesaikan dua kasus matriks.

## Output
- Solusi sistem.
- Invers matriks.
- Condition number.

## Kesimpulan
Condition number digunakan untuk menilai sensitivitas matriks terhadap galat pembulatan.

---

# Soal 11.17

## Deskripsi
Menyelesaikan sistem persamaan nonlinear.

## Metode
- Menggunakan fungsi nonlinear.
- Menyelesaikan dengan `scipy.optimize.fsolve()`.

## Output
- Dua solusi nonlinear.

## Kesimpulan
Sistem nonlinear berhasil diselesaikan dengan tebakan awal yang berbeda.

---

# Soal 11.18

## Deskripsi
Menentukan jumlah transistor, resistor, dan chip berdasarkan ketersediaan material.

## Metode
- Menyusun sistem persamaan linear.
- Menyelesaikan menggunakan metode matriks.

## Output
- Jumlah transistor.
- Jumlah resistor.
- Jumlah chip.

## Kesimpulan
Model linear berhasil digunakan untuk menentukan jumlah produk yang dapat dibuat.

---

# Soal 11.19

## Deskripsi
Menganalisis matriks Hilbert orde 10.

## Metode
- Membentuk matriks Hilbert.
- Menghitung condition number.
- Mengestimasi digit yang hilang.
- Menyelesaikan sistem linear.

## Output
- Condition number.
- Perkiraan digit hilang.
- Solusi sistem.

## Kesimpulan
Matriks Hilbert sangat sensitif terhadap galat pembulatan sehingga merupakan contoh matriks ill-conditioned.

---

# Soal 11.20

## Deskripsi
Menganalisis matriks Hilbert orde 6 dan membandingkan solusi numerik dengan solusi sebenarnya.

## Metode
- Membentuk matriks Hilbert.
- Menghitung condition number.
- Menghitung error hasil solusi.

## Output
- Condition number.
- Solusi numerik.
- Error.

## Kesimpulan
Matriks Hilbert orde 6 masih dapat diselesaikan dengan akurasi yang baik dibandingkan orde 10.

---

# Soal 11.21

## Deskripsi
Membentuk matriks augmented [A|I].

## Metode
- Menyusun matriks A.
- Menyusun matriks identitas.
- Menggabungkan keduanya secara horizontal.

## Output
- Matriks A.
- Matriks identitas.
- Matriks augmented.

## Kesimpulan
Matriks augmented terbentuk dengan menggabungkan matriks koefisien dan identitas.

---

# Soal 11.22

## Deskripsi
Menyusun sistem persamaan linear ke dalam bentuk matriks dan menghitung transpose serta inversnya.

## Metode
- Menyusun matriks koefisien A.
- Menentukan vektor b.
- Menyelesaikan sistem.
- Menghitung transpose dan invers.

## Output
- Solusi x₁, x₂, x₃.
- Transpose matriks.
- Invers matriks.

## Kesimpulan
Operasi matriks dasar berhasil diterapkan pada sistem persamaan linear.

---

# Soal 11.23

## Deskripsi
Membandingkan jumlah operasi antara Gaussian Elimination dan Thomas Algorithm.

## Metode
- Menghitung pendekatan operasi untuk n = 2 sampai 20.
- Membuat grafik perbandingan.

## Output
- Grafik perbandingan jumlah operasi.

## Kesimpulan
Thomas Algorithm lebih efisien untuk sistem tridiagonal karena kompleksitasnya lebih rendah.

---

# Soal 11.24

## Deskripsi
Membuat program Thomas Algorithm untuk sistem tridiagonal dan menguji dengan Example 11.1.

## Metode
- Forward Elimination.
- Back Substitution.
- Menggunakan data Example 11.1.

## Output
- T₁ = 65.970
- T₂ = 93.778
- T₃ = 124.538
- T₄ = 159.480

## Kesimpulan
Program berhasil mereproduksi hasil Example 11.1 pada buku.

---

# Soal 11.25

## Deskripsi
Membuat program Cholesky Decomposition dan menguji dengan Example 11.2.

## Metode
- Implementasi manual algoritma Cholesky.
- Memverifikasi hasil dengan A = LLᵀ.

## Output
- Matriks L.
- Verifikasi hasil perkalian L dan Lᵀ.

## Kesimpulan
Program berhasil mereproduksi hasil Example 11.2.

---

# Soal 11.26

## Deskripsi
Membuat program Gauss-Seidel dan menguji dengan Example 11.3.

## Metode
- Iterasi Gauss-Seidel.
- Menghitung error relatif aproksimasi.
- Menghentikan iterasi ketika toleransi terpenuhi.

## Output
- x₁ = 3
- x₂ = -2.5
- x₃ = 7

## Kesimpulan
Program berhasil mereproduksi hasil Example 11.3.

---

# Soal 11.27

## Deskripsi
Menyelesaikan persamaan diferensial steady-state mass balance menggunakan metode beda hingga.

Persamaan:

0 = D(d²c/dx²) − U(dc/dx) − kc

Dengan:
- D = 2
- U = 1
- k = 0.2
- c(0) = 80
- c(10) = 20
- Δx = 2

## Metode
- Menggunakan finite difference method.
- Mengubah persamaan diferensial menjadi sistem aljabar linear.
- Menyelesaikan sistem dengan `numpy.linalg.solve()`.
- Membuat plot konsentrasi terhadap jarak.

## Output
- Konsentrasi pada x = 0, 2, 4, 6, 8, dan 10.
- Grafik concentration vs distance.

## Kesimpulan
Konsentrasi berhasil dihitung dan divisualisasikan sepanjang kanal.

---

# Soal 11.28

## Deskripsi
Menyelesaikan sistem persamaan linear pentadiagonal.

## Metode
- Menyusun matriks pentadiagonal.
- Melakukan forward elimination tanpa pivoting.
- Melakukan back substitution.

## Output
- x₁
- x₂
- x₃
- x₄
- x₅

## Kesimpulan
Sistem pentadiagonal berhasil diselesaikan menggunakan algoritma eliminasi khusus.

---
