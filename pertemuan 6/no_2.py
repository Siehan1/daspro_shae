print("===== Aplikasi Ganjil Genap =====")
print("=================================")

angka = input("Masukkan Angka :")
print("=================================")

if(angka.isdigit()):
    angka = int(angka)
    if(angka % 2 == 0):
        print(f"Angka {angka} merupakan angka Genap")
        pass
    else:
        print(f"Angka {angka} merupakan angka Ganjil")
else:
    print("Masukkan Angka")