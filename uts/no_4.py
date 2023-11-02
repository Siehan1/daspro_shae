nim = int(input("Masukan Tiga Digit Terakhir NIM: "))
if 0<nim and nim<51 and nim%2 == 0 :
    print("Silahkan masuk ke kelas K2")
elif 0<nim and nim<51 and nim%2 == 1 :
    print("Silahkan masuk ke kelas K1")
else :
    if (51<nim and nim<101) and nim%2 == 0 :
        print("Silahkan masuk ke kelas K4")
    elif (51<nim and nim<101) and nim%2 == 1:
        print("Silahkan masuk ke kelas K3")
    else:
        if 101<nim and nim<150 and nim%2 == 0 :
            print("Silahkan masuk ke kelas K6")
        elif 101<nim and nim<150 and nim%2 == 1:
            print("Silahkan masuk ke kelas K5")
        else:
            if nim>151 and nim%2 == 0 :
                print("Silahkan masuk ke kelas K8")
            else:
                print("Silahkan masuk ke kelas K7")