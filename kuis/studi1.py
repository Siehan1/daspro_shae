inventori = {
    "barang1":{
        "nama" : "Pensil",
        "harga" : 4000,
        "stok" : 10
    },
    "barang2" :{
        "nama" : "Pulpen",
        "harga" : 5000,
        "stok" : 6
    },
    "barang3" :{
        "nama" : "Buku",
        "harga" : 4500,
        "stok" : 0
    },
    "barang4" :{
        "nama" : "Penggaris",
        "harga" : 2000,
        "stok" : 4
    },
    "barang5" :{
        "nama" : "Penghapus",
        "harga" : 1000,
        "stok" : 8
    }
}

i = 1
for x in inventori:
    print(f"{i}. {inventori[x]['nama']}, harga : {inventori[x]['harga']}")
    i+=1


barang = int(input("Pilih yang ingin dibeli (1/2/3/...): "))
jumlah = int(input("Jumlah yang ingin dibeli: "))
y=1
for x in inventori:
    if barang == y:
        if jumlah <= inventori[x]["stok"]:    
            inventori[x]["stok"] = inventori[x]["stok"] - jumlah
            print(f"Barang yang dibeli: {inventori[x]['nama']}")
            print("Jumlah yang harus dibayar:",inventori[x]["harga"]*jumlah)

            break
        else:
            print("Stok barang tidak ada/Tidak mencukupi!")
            break
    else:
        y+=1
        if y>len(inventori):
            print("Pilihan Tidak Tersedia!")