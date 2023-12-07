#Nama   : Shaehyan Samukti
#NIM    : 2301461
#Kelas  : RPL-1A

def bubbbleSort(array):
    n = len(array)

    for i in range(n):
        for j in range(n - i - 1):
            if (array[j] > array[j + 1]):
                array[j], array[j + 1] = array[j + 1], array[j]

    return array

array = []
banyak_array = int(input("Masukkan jumlah array: "))
for i in range(0, banyak_array):
    nilai = int(input("Masukkan nilai array: "))
    array.append(nilai)

print(f"Array sebelum disortir:{array}")
print(f"Array setelah disortir:{bubbbleSort(array)}")