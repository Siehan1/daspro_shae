nilai = [90,86,57,59,95,77,67,94,82,86]

noUrut = int(input("Masukkan No Urut Siswa: "))

i=1
for x in nilai:
    if(noUrut == i):
        print(f"Siswa dengan nomor urut {i} mempunyai nilai {nilai[i-1]}")
        break
    else:
        i+=1
        if(i > len(nilai)):
            print("nomor urut tidak ada!")