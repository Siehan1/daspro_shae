hasil = 0
list_bilangan = []

while True:
    bilangan = int(input("input: "))

    index = len(list_bilangan)
    list_bilangan.append(bilangan)

    # if index == 0:
    #     continue

    if list_bilangan[index] > list_bilangan[index -1]:
        hasil += bilangan

    if index > 3:
        if list_bilangan[index] <= list_bilangan[index -1]:
            if list_bilangan[index -1] <= list_bilangan[index -2]:
                if list_bilangan[index -2] <= list_bilangan[index -3]:
                    break

print(f"Hasil penjumlahan nilai yang mengecil: {hasil}")





