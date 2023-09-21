buah = ["apel","jeruk","ceri","durian","apel","mangga"]
print(buah)

print(buah[2:5])#1. mengambil items list dari indeks ke 2 sampai 5

buah.pop(4)#2. menghapus item "apel"
print(buah)

buah[2] = "cherry"#3. mengubah item "ceri" menjadi "cherry"
print(buah)

buah.insert(3,"strawberry")#4. menambahkan item "strawberry" pada indeks ke 3
print(buah)

buah.sort()#5. mengurutkan items sesuai abjad
print(buah)
