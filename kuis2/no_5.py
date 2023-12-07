def linearSearch(menu, cari_menu):
    for i in range(len(menu)):
        if menu[i] == cari_menu:
            return i
    return -1
    
cari_menu = str(input("Silahkan Cek Ketersediaan Menu: "))
menu = ["Ayam Gulai", "Babat", "Cumi", "Ikan Kembung", "Kikil", "Limpa", "Otak", "Paru", "Rendang", "Telur", "Usus"]

result = linearSearch(menu, cari_menu)

if (result != -1):
    print(f"{cari_menu} Tersedia, Silahkan Antri untuk Memesan")
else:
    print(f"Maaf, {cari_menu} Tidak tersedia")