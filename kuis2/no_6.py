dataSiswa = {}
def bubbbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if (array[j] < array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

banyak_siswa = int(input("Masukkan jumlah siswa: "))
for i in range(0, banyak_siswa):
    nama = input("Masukkan nama siswa: ")
    nilaiAkhir = int(input("Masukkan nilai akhir: "))
    dataSiswa[nilaiAkhir] = nama

nilai_sort = bubbbleSort(list(dataSiswa.keys()))
for x in nilai_sort:
    print(dataSiswa[x])
# nama = list(dataSiswa.values())
# print(nama)