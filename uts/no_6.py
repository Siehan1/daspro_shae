banyak_bilangan = int(input("Masukan banyak bilangan: "))
bilangan_bukan_prima = 0
for x in range(0, banyak_bilangan):
    bilangan = int(input(f"Masukan bilangan ke-{x+1}: "))
    
    prima = True
    for x in range(2, bilangan):
        if(bilangan % x == 0 ):
            prima = False
            break
    if prima == True:
        bilangan_bukan_prima += bilangan

print("Hasil penjumlahan bilangan bukan prima", bilangan_bukan_prima)