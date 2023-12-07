#Nama   : Shaehyan Samukti
#NIM    : 2301461
#Kelas  : RPL-1A

buku = {
    1:{
        "kodeBuku" : "001",
        "judul" : "Hujan",
        "penulis" : "Tere Liye",
        "status" : "Tersedia"
    },
    2:{
        "kodeBuku" : "002",
        "judul" : "Bumi",
        "penulis" : "Tere Liye",
        "status" : "Tersedia"
    }
}
def main():
    print("===== SELAMAT DATANG DI PERPUSTAKAAN JENDELA DUNIA =====")
    print("")
    print("1. Tambah Buku           4. Lihat Buku Tersedia")
    print("2. Pinjam Buku           5. Lihat Buku Dipinjam")
    print("3. Kembalikan Buku")
    pilihan = input("(1,2,3,4,5)> ")
    
    if pilihan == "1":
        tambah_buku()
    elif pilihan == "2":
        pinjam_buku()
    elif pilihan == "3":
        kembalikanBuku()
    elif pilihan == "4":
        lihatBuku()
    elif pilihan == "5":
        lihatBukuPinjam()

def tambah_buku():
    
    print("===== Menu Tambah Buku =====")
    judul = input("Judul Buku: ")
    penulis = input("Penulis Buku: ")
    kode = input("Kode Buku: ")
    status = "Tersedia"

    next_index = len(buku) + 1
    buku[next_index] = {
        "kodeBuku": kode,
        "judul": judul,
        "penulis": penulis,
        "status": status
    }
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()

def pinjam_buku():
    print("===== Menu Pinjam =====")
    for x in range(1,len(buku)+1):
        print(f"{x}. {buku[x]['judul']}")
    
    print("Pilih buku yang akan dipinjam")
    input1 = int(input("(1,2,3,...)> "))
    if buku[input1]["status"] == "Tersedia":
        buku[input1]["status"] = "Dipinjam"
        print(f"Anda meminjam buku {buku[input1]['judul']}")
    else:
        print(f"Buku {buku[input1]['judul']} sedang dipinjam")

    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()

def lihatBuku():
    print("===== Menu Liaht Buku Tersedia =====")
    print("Buku yang tersedia:")
    for x in range(1,len(buku)+1):
        if buku[x]["status"] == "Tersedia":
            print(f"- {buku[x]['judul']}")
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()

def lihatBukuPinjam():
    print("===== Menu Lihat Buku Dipinjam =====")
    print("Buku yang sedang dipinjam:")
    for x in range(1,len(buku)+1):
        if buku[x]["status"] == "Dipinjam":
            print(f"- {buku[x]['judul']}")
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()

def kembalikanBuku():
    print("===== Menu Kembalikan Buku =====")
    for x in range(1,len(buku)+1):
        if buku[x]["status"] == "Dipinjam":
            print(f"{x}. {buku[x]['judul']}")
    
    print("Pilih buku yang akan dipinjam")
    input1 = int(input("(1,2,3,...)> "))
    buku[input1]["status"] == "Tersedia"
    print(f"Anda mengembalikan buku {buku[input1]['judul']}")
    
    input2 = input("Kembali ke menu awal, ketik yes: ")
    if input2 == "yes":
        main()
print(main())