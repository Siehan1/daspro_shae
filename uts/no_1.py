print("SIlahkan Login")

for i in range(1,4):
    username = input("Username: ")
    password = input("Password: ")
    if (username != "utsdaspro" and password != "rpl2023"):
        print(f"Login Salah! Kesempatan Anda sisa {3-i}")
    else:
        print("Login Berhasil! Selamat Datang di Aplikasi prodi RPL")
        break

    if 3-i == 0:
        print("Anda Tidak tiperkenankan mengakses apliaksi ini")





