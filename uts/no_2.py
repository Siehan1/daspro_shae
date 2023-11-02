bilangan_genap = 0
bilangan_ganjil = 0

while True:
    bilangan = int(input("Masukkan bilangan: "))
    if(bilangan < 0):
        break
    if(bilangan == 0 or bilangan % 2 == 0):
        bilangan_genap += bilangan
    else:
        bilangan_ganjil += bilangan

print(f"Jumlah bilangan genap: {bilangan_genap}")
print(f"Jumlah bilangan ganjil: {bilangan_ganjil}")
