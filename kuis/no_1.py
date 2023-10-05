nilai = {
    "1": 90,
    "2": 86,
    "3": 57,
    "4": 59,
    "5": 95,
    "6": 77,
    "7": 67,
    "8": 94,
    "9": 82,
    "10": 86
}

noUrut = int(input("Masukkan No Urut Siswa: "))

i=1
for x in nilai:
    if(noUrut == i):
        print(f"Siswa dengan nomor urut {x} mempunyai nilai {nilai[x]}")
        break
    else:
        i+=1
        if(i > len(nilai)):
            print("nomor urut tidak ada!")