print("===== Aplikasi Beasiswa =====")
print("=============================")

nilai = input("Masukkan Nilai (angka): ")
while (not nilai.isdigit()):
    nilai = input("dalam angka: ")
nilai = int(nilai)

gaji = input("Masukkan Penghasilan Ortu (tidak dengan simbol ', . * '): ")
while (not gaji.isdigit()):
    gaji = input("Hanya Angka: ")
gaji = int(gaji)

if((nilai > 80) and gaji < 4000000):
    print("Selamat, Kamu diterima beasiswa")
else:
    print("Anda kurang beruntung")