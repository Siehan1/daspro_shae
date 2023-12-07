#Nama   : Shaehyan Samukti
#NIM    : 2301461
#Kelas  : RPL-1A

def linearSearch(array, cari):
    for i in range(len(array)):
        if array[i] == cari:
            return i
    return -1

array = []
banyak_array = int(input("Masukkan jumlah array: "))
for i in range(0, banyak_array):
    nilai = int(input("Masukkan nilai array: "))
    array.append(nilai)

cari = int(input("Masukkan nilai yang akan dicari: "))
hasil = linearSearch(array, cari)

if (hasil != -1): 
    print (f"{cari} Ada dalam daftar angka dengan index ke-{hasil}") 
else: 
    print (f"{cari} Tidak ada dalam daftar angka")