# Nama: Shaehyan Samukti
# NIM: 2301461
# Soal nomor: 3
import time

start_time = time.time()
def linearSearch(array, cari):
    for i in range(len(array)):
        if array[i] == cari:
            return i
    return -1

array = [1, 2, 5, 7, 8, 10, 16, 18, 19, 23, 24, 26, 28, 29, 32, 33,
         34, 35, 36, 38, 40, 41, 42, 43, 44, 46, 48, 49, 51, 55, 57,
         58, 59, 60, 63, 65, 66, 69, 74, 75, 76, 77, 78, 79, 81, 82,
         85, 90, 93, 100]

cari = 60
hasil = linearSearch(array, cari)

if (hasil != -1): 
    print (f"{cari} Ada dalam daftar angka") 
else: 
    print (f"{cari} Tidak ada dalam daftar angka")

print(f"Process finished: {time.time() - start_time} seconds")