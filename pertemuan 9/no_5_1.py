def nilai_mutak(angka = 0):
    if angka < 0:
        return -angka
    return angka

def selisih(a, b):
    return nilai_mutak(a - b)

print("Input Mulai: ")
jam_1 = int(input("Jam: "))
menit_1 = int(input("Menit: "))
detik_1 = int(input("Detik: "))


print("Input Selesai: ")
jam_2 = int(input("Jam: "))
menit_2 = int(input("Menit: "))
detik_2 = int(input("Detik: "))

print(selisih(jam_1,jam_2))
print(selisih(menit_1,menit_2))
print(selisih(detik_1,detik_2))