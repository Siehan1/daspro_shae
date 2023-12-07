def main():
    print("|SELAMAT DATANG DI PERPUSTAKAAN UPI|")
    print("")
    print("|Tambah Buku|Pinjam Buku|Kembalikan Buku|Lihat Buku|Lihat Buku Yang Dipinjam|")
    pilihan = input("> ")
    
    if pilihan == "Tambah Buku":
        tambahBuku()
    elif pilihan == "Pinjam Buku":
        pinjamBuku()
    elif pilihan == "Lihat Buku":
        lihatBuku()
    elif pilihan == "Lihat Buku Yang Dipinjam":
        lihatBukuPinjam()

buku1 = {
    "judul" : "Andromeda",
    "penulis" : "Jeje",
    "kode" : "2301",
    "status" : "Tersedia"
}

buku2 = {
    "judul" : "Mataharoy",
    "penulis" : "Lopi",
    "kode" : "2302",
    "status" : "Dipinjam"
}

buku3 = {
    "judul" : "Sagitarus",
    "penulis" : "Luna",
    "kode" : "2303",
    "status" : "Dipinjam"
}

buku4 = {
    "judul" : "",
    "penulis" : "",
    "kode" : "",
    "status" : "Tersedia"
}

def tambahBuku():
    print("|MENU TAMBAH BUKU|")
    judul = input("Judul Buku: ")
    penulis = input("Penulis Buku: ")
    kode = input("Kode Buku: ")
    
    buku4.update({f"judul": {judul}})
    buku4.update({f"penulis": {penulis}})
    buku4.update({f"kode": {kode}})
    print("")
    print(buku4)
    print("")
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
        
def pinjamBuku():
    print("|MENU PINJAM BUKU|")
    print(buku1)
    print(buku2)
    print(buku3)
    print(buku4)
    
    while True:
        print("|BUKU 1|BUKU 2|BUKU 3|BUKU 4|")
        input3 = input("> ")
        if input3 == "BUKU 1":
            if buku1["status"] == "Tersedia":
                buku1.update({f"status": "Dipinjam"})
                print(buku1)
                break
            else:
                print("Buku sedang dipinjam")
        elif input3 == "BUKU 2":
            if buku2["status"] == "Tersedia":
                buku2.update({f"status": "Dipinjam"})
                print(buku2)
                break
            else:
                print("Buku sedang dipinjam")
        elif input3 == "BUKU 3":
            if buku3["status"] == "Tersedia":
                buku3.update({f"status": "Dipinjam"})
                print(buku3)
                break
            else:
                print("Buku tidak dipinjam")
        elif input3 == "BUKU 4":
            if buku4["status"] == "Tersedia":
                buku4.update({f"status": "Dipinjam"})
                print(buku4)
                break
            else:
                print("Buku tidak dipinjam")
        else:
            pass
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
        
def kembalikanBuku():
    print("|MENU KEMBALIKAN BUKU|")
    print(buku1)
    print(buku2)
    print(buku3)
    print(buku4)
    
    while True:
        print("|BUKU 1|BUKU 2|BUKU 3|BUKU 4|")
        input3 = input("> ")
        if input3 == "BUKU 1":
            if buku1["status"] == "Tersedia":
                print("Buku tidak dipinjam")
            else:
                buku1.update({f"status": "Tersedia"})
                print(buku1)
                break
        elif input3 == "BUKU 2":
            if buku2["status"] == "Tersedia":
                print("Buku tidak dipinjam")
            else:
                buku2.update({f"status": "Tersedia"})
                print(buku2)
                break
        elif input3 == "BUKU 3":
            if buku3["status"] == "Tersedia":
                print("Buku tidak dipinjam")
            else:
                buku3.update({f"status": "Tersedia"})
                print(buku3)
                break
        elif input3 == "BUKU 4":
            if buku4["status"] == "Tersedia":
                print("Buku tidak dipinjam")
            else:
                buku4.update({f"status": "Tersedia"})
                print(buku4)
                break
        else:
            pass
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
    
def lihatBuku():
    print("|MENU LIHAT BUKU|")
    
    def lihat():
        if buku1["status"] == "Tersedia":
            print(buku1)
        if buku2["status"] == "Tersedia":
            print(buku2)
        if buku3["status"] == "Tersedia":
            print(buku3)
        if buku4["status"] == "Tersedia":
            print(buku4)
        else:
            pass
    
    print(lihat())
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
        
def lihatBukuPinjam():
    print("|MENU LIHAT BUKU YANG DIPINJAM|")
    
    def lihat():
        if buku1["status"] == "Dipinjam":
            print(buku1)
        if buku2["status"] == "Dipinjam":
            print(buku2)
        if buku3["status"] == "Dipinjam":
            print(buku3)
        if buku4["status"] == "Dipinjam":
            print(buku4)
        else:
            pass
    
    print(lihat())
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
    
print(main())