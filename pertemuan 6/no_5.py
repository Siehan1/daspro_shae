print("===== Hemat Berkah =====")
print("========================")

belanja = input("Masukkan total belanja: ")

i=True
while(i==True):
    if(belanja.isdigit()):
        belanja = int(belanja)
        i = False

        if(belanja > 500000):
            diskon = belanja * (10 / 100)
            totalBelanja = belanja - diskon

            print(f"Total yang harus dibayar: {int(totalBelanja)}")
            print(f"Diskon: {int(diskon)}")
        else:
            diskon = 0
            print(f"Total yang harus dibayar: {int(belanja)}")
            print(f"Diskon: {int(diskon)}")
    else:
        belanja = input("Hanya masukka angka: ")
        i = True