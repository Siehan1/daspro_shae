def penjumlahan(a,b,c):
    hasil = a+b+c
    print(f"Hasil dari penjumlahan {a} + {b} + {c} = {hasil}")

def perkalian(a,b,c):
    hasil = a*b*c
    print(f"Hasil dari perkalian {a} * {b} * {c} = {hasil}")

print("==Kalkulator Sederhana 3 digit==") 
print("================================")
i=0
while i<1:
    a = int(input("Masukkan Bilangan Pertama :"))
    b = int(input("Masukkan Bilangan Kedua   :"))
    c = int(input("Masukkan Bilangan Ketiga  :"))
    print("================================")
    print("1. Penjumlahan 2. Perkalian")

    pilih = int(input("Pilih salah satu (1/2) :"))
    match pilih:
        case 1:
            penjumlahan(a,b,c)
        case 2:
            perkalian(a,b,c)
        case default:
            print("Masukkan pilihan dengan benar")
    lanjut = input("Lanjut? (Y/N) ")
    if lanjut == "y" or lanjut == "Y":
        i=0
    else:
        i=1