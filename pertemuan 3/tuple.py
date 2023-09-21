buah = ("apel","jeruk","ceri","durian","apel","mangga")
print(buah)

print(buah[2:5])#1. mengambil items tuple dari indeks ke 2 sampai 5

x = list(buah)#2. mengubah tuple menjadi list lalu menghapus item pada "durian"
x.pop(3)
buah = tuple(x)
print(buah)

x = list(buah)#3. mengubah tuple menjadi list lalu menambahkan item antara "jeruk" dan "ceri"
x.insert(2,"manggis")
buah = tuple(x)
print(buah)