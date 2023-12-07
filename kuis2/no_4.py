#Nama   : Shaehyan Samukti
#NIM    : 2301461
#Kelas  : RPL-1A

antrian_klinik = []
kapasitas_antrian = 10

def ambil_antrian():
    if len(antrian_klinik) < kapasitas_antrian:
        nomor_antrian = len(antrian_klinik) + 1
        antrian_klinik.append(nomor_antrian)
        print("Nomor antrian Anda: ",nomor_antrian)
    else:
        print("\nMohon maaf, antrian penuh. Silakan datang kembali lagi nanti.")

def tampilkan_antrian():
    if len(antrian_klinik) == 0:
        print("Saat ini  belum  ada antrian")
    else:
        print(f"Antrian saat ini: ")
        for nomor in antrian_klinik:
            print(nomor)

while True:
    print("\n===== SELAMAT DATANG DI KLINIK CNTA KASIH =====")
    print("Silahkan pilih menu dengan menggunakan kode angka (1/2)")
    print("1. Ambil Antrian")
    print("2. Tampilkan Antrian")

    pilihan = input("Pilih menu : ")

    if pilihan == '1':
        ambil_antrian()
    elif pilihan == '2':
        tampilkan_antrian()
    else:
        print("Pilihan tidak valid. Silakan pilih lagi.")
    
    selesai = input("Lanjut?(Y/N)")
    if selesai == "N":
        print("Terima kasih, keluar dari program.")
        break
