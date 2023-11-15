def pertama(jari2, tinggi):
    hasil = 22/7 * (jari2 ** 2) * tinggi
    return hasil

def kedua(jari2, tinggi):
    hasil = 3.14 * (jari2 **2) * tinggi
    return hasil

inputJariJari = int(input("Masukan besar Jari-Jari: "))
inputTInggi = int(input("Masukan besar Tinggi: "))

if (inputJariJari % 7) == 0:
    print(f"Volume Tabung: {pertama(inputJariJari, inputTInggi)}")
else:
    print(f"Volume Tabung: {kedua(inputJariJari, inputTInggi)}")