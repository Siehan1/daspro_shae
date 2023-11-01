print("===== BONUS KARYAWAN =====")
print("==========================")

performa = input("Masukkan Performa kerja Anda (sangat baik/cukup): ")
gaji = input("Masukkan Gaji Anda (angka saja): ")

i=True
while(i==True):
    if(gaji.isdigit()):
        gaji = int(gaji)
        i=False
        if(performa == "sangat baik"):
            bonus = gaji * (20 / 100)
            totalGaji = gaji + bonus
            print("==========================")
            print(f"Bonus gaji: {int(bonus)}")
            print(f"Total gaji + bonus: {int(totalGaji)}")
        elif(performa == "cukup"):
            bonus = gaji * (10 / 100)
            totalGaji = gaji + bonus
            print("==========================")
            print(f"Bonus gaji: {int(bonus)}")
            print(f"Total gaji + bonus: {int(totalGaji)}")
        else:
            bonus = gaji * (5 / 100)
            totalGaji = gaji + bonus
            print("==========================")
            print(f"Bonus gaji: {int(bonus)}")
            print(f"Total gaji + bonus: {int(totalGaji)}")
    else:
        gaji = input("Masukkan Gaji dengan Angka: ")
        i=True

