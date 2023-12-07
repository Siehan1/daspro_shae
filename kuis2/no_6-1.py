jumlah_siswa = int(input("Masukkan jumlah siswa: "))
    
    # Membuat list untuk menyimpan nama dan nilai siswa
nama_nilai_siswa = []
for i in range(jumlah_siswa):
    nama = input(f"Masukkan nama siswa ke-{i + 1}: ")
    nilai = int(input(f"Masukkan nilai {nama}: "))
    nama_nilai_siswa.append((nama, nilai))


nama_siswa = [(nama, nilai) for nama, nilai in nama_nilai_siswa]
for x in range(len(nama_siswa)):
    print(nama_siswa[x][1])
