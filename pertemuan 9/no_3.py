def jumlah(*bilangan):
    total = 0
    for angka in bilangan:
        total = total + angka

    rataRata = total / len(bilangan)
    return total, rataRata

inputBilangan = input("Masukkan angka, pisahkan dengan tanda koma: ")
bilangan = list(map(int, inputBilangan.split(",")))

hasil_total, hasil_rata_rata = jumlah(*bilangan)

formatted_bilangan = ' + '.join(map(str, bilangan))

print(f"Total = {formatted_bilangan} = {hasil_total}")
print(f"Rata-Rata = {hasil_total}/{len(bilangan)} = {hasil_rata_rata}")