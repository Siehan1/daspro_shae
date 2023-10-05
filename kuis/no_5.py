tinggi = 400
lebar = 1000
panjang = 8
harga = 520000

tinggiM = tinggi / 100
lebarM = lebar / 100

luas = int((2 * (panjang * tinggiM)) + (2 * (lebarM * tinggiM)))

hargaTotal = harga * luas

print(f"Luas bangunan yang pak Abi bangun seluas {luas} m2")
print(f"Total biaya yang Pak Abi harus keluarkan untuk membuat bangunan tersebut adalah Rp. {hargaTotal}")