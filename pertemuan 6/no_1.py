print("===== Aplikasi Cek Nilai =====")
print("==============================")

nilai = input("Masukkan Nilai : ")

if(nilai.isdigit()):
    nilai = int(nilai)
    if(nilai<=100):
        if(nilai>=90):
            print(f"Kategori nilai anda adalah A")
        elif(nilai<90 and nilai>=80):
            print(f"Kategori nilai anda adalah B")
        elif(nilai<80 and nilai>=70):
            print(f"Kategori nilai anda adalah C")
        else:
            print(f"Kategori nilai anda adalah D")
    else:
        print("Mohon Masukkan Nilai Dengan Serius")
else:
    print("Jangan Masukkan Huruf")