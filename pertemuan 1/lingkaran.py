phi = 3.14

def luas(jari2):
    luas = phi * (jari2 ** 2)
    print("Luas Lingkaran adalah :",luas)

def keliling(jari2):
    keliling = phi * (jari2 * 2)
    print("Keliling Lingkaran adalah :",keliling)

print("===== Menghitung Luas dan Keliling Lingkaran =====")
print("==================================================")

jari2 = float(input("Masukkan Jari Jari Lingkaran: "))
pilih = input("menghitung luas atau keliling?")
print("==================================================")

if(pilih == "luas" or pilih == "Luas"):
    luas(jari2)
elif(pilih == "keliling" or pilih == "Keliling"):
    keliling(jari2)