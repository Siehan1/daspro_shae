print("Silahkan login")

def login():
    username = input("Username: ")
    password = input("Password: ")
    for i in range(1,4):
        if (password != "Latihan"):
            if 3-i == 0:
                print("Anda Tidak tiperkenankan mengakses apliaksi ini")
                break
            print(f"Password Salah! Kesempatan Anda sisa {3-i}x lagi")
            print(f"Username: {username}")
            password = input("Password: ")
        else:
            print("Login Berhasil! Selamat Datang di Aplikasi LabKom SMAN 2 Harapan")
            break
     
login()