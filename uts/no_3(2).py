ayam = int(input("Anak ayam turunlah "))
print(f"Mati satu tinggalah {ayam-1}")
print("")
while ayam:
    print(f"Anak ayam turunlah {ayam-1}")
    if (ayam -1 ) == 1:
        print("Mati satu tinggalah Induknya")
        break
    print(f"Mati satu tinggalah {ayam-2}")
    print("")

    ayam -= 1
