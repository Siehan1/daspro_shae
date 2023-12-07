dataSiswa = {}

def bubbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if array[j][1] < array[j + 1][1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

banyak_siswa = int(input("Masukkan jumlah siswa: "))
for i in range(banyak_siswa):
    nama = input("Masukkan nama siswa: ")
    while True:
        try:
            nilaiAkhir = int(input("Masukkan nilai akhir: "))
            break
        except ValueError:
            print("Masukkan angka yang valid.")

    dataSiswa[nama] = nilaiAkhir

# Sorting based on values (nilaiAkhir)
sorted_array = bubbleSort(list(dataSiswa.items()))

# Searching for a student's rank
inputNama = input("Cari Nama Siswa: ")
result = -1

# Linear search modified for tuple comparison
for i in range(len(sorted_array)):
    name, _ = sorted_array[i]
    if name == inputNama:
        result = i + 1
        break

if result != -1:
    print(f"Nama {inputNama} memiliki nilai {dataSiswa[inputNama]} dan berada di peringkat {result}")
else:
    print(f"{inputNama} tidak tersedia dalam data siswa.")