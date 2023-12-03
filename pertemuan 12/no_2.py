# Nama: Shaehyan Samukti
# NIM: 2301461
# Soal nomor: 2

def search(array, cari):
    indexLow, indexHigh = 0, len(array) - 1
    
    while indexLow <= indexHigh:
        middle = (indexHigh + indexLow) // 2
        middleValue = array[middle]

        if middleValue == cari:
            return middle
        elif middleValue < cari:
            indexLow = middle + 1
        else:
            indexHigh = middle -1
    return -1

namaMhs = ["Yoga", "Ayu", "Hilal", "Anggi",
           "Agus", "Yogi" , "Arya", "Amel",
           "Andi", "Bayu", "Bagas", "Budi",
           "Bagus", "Citra", "Nisa", "Chika",
           "Rizky", "Bastian", "Cakra", "Ben"]

namaMhs = sorted(namaMhs)
cariNama = input("Cari nama mahasiswa (Huruf depan kapital): ")

hasil = search(namaMhs, cariNama)

if (hasil != -1): 
    print (f"{cariNama} merupakan mahasiswa aktif") 
else: 
    print (f"{cariNama} tidak terdaftar sebagai mahasiswa aktif")