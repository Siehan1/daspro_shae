mobil  = {
    "Merk": "Honda",
    "Tipe" : "HRV",
    "Tahun" : "2018",
    "Warna" : "hitam",
    "No polisi" : "D 1234 ABC",
    "Bensin" : "Pertalite",
    "Transmisi" : "Manual"
}
print("Mobil Lama Pak Oki Adalah:")
for x in mobil:
    print(f"{x} : {mobil[x]}")
print("-------------------------------------")
print("Masukkan informasi detail mobil baru:")
mobil["Merk"] = input("Merk: ")
mobil["Tipe"] = input("Tipe: ")
mobil["Tahun"] = input("Tahun: ")
mobil["Warna"] = input("Warna: ")
mobil["No polisi"] = input("No. Polisi: ")
mobil["Bensin"] = input("Bensin: ")
mobil["Transmisi"] = input("Transmisi: ")

print("=====================================")
print("Mobil baru Pak Oki Adalah:")
for x in mobil:
    print(f"{x} : {mobil[x]}")
