# Nama: Shaehyan Samukti
# NIM: 2301461
# Soal nomor: 1

def search(array, cari):
    for i in range(len(array)):
        if array[i] == cari:
            return i
    return -1

barang = ['Buku', 'Pensil', 'Pensil Warna', 
          'Kertas Origami', 'Pensil', 'Kertas HVS', 
          'Penghapus', 'Penggaris', 'Spidol', 
          'Kanvas Lukis', 'Cat Air', 'Penggaris Segitiga',
          'Stabilo', 'Sticker', 'Penggaris Jangka']

print("===== S'MART =====")
cari = input("Cari barang: ")
hasil = search(barang, cari)

if (hasil != -1): 
    print (f"Stok {cari} masih ada") 
else: 
    print (f"Stok {cari} sudah habis")