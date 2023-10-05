barangjuli = ["T-shirt","Blouse", "Kemeja", "Celana Panjang", "Rok", "Baju Renang", "Tas", "Topi", "Sepatu", "Sendal"]

print("daftar barang pada bulan Juli:")
for x in barangjuli:
    print("-",x)
print(f"jumlah barang ada {len(barangjuli)} item")

barangjuli[5] = "Gamis"
barangjuli.append("Ikat rambut")
barangjuli.append("Kerudung")

print("============================")
print("daftar barang pada bulan ini:")
for x in barangjuli:
    print("-",x)
print(f"jumlah barang ada {len(barangjuli)} item")