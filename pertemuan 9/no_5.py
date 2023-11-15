def hitung_jam(jam_a, jam_b):
    jam = jam_b - jam_a
    return jam

def hitung_menit(menit_a, menit_b, jam):
    if menit_a > menit_b:
        menit = (menit_b + 60) - menit_a
        jam -= 1
    else:
        menit = menit_b - menit_a
    return {"menit": menit, "jam": jam}

def hitung_detik(detik_a, detik_b, menit):
    if detik_a > detik_b:
        detik = (detik_b + 60) - detik_a
        if menit["menit"] == 0:
            menit["menit"] += 59
            menit["jam"] -= 1
        else:
            menit["menit"] -= 1
    else:
        detik = detik_b - detik_a
    return {"detik": detik, "menit": menit['menit']}

print("Input Mulai: ")
jam_a = int(input("Jam: "))
menit_a = int(input("Menit: "))
detik_a = int(input("Detik: "))

print("Input Selesai: ")
jam_b = int(input("Jam: "))
menit_b = int(input("Menit: "))
detik_b = int(input("Detik: "))

jam_result = hitung_jam(jam_a, jam_b)
menit_result = hitung_menit(menit_a, menit_b, jam_result)
detik_result = hitung_detik(detik_a, detik_b, menit_result)

print("Hitung Selisih:")
print(f"{menit_result['jam']} Jam - {detik_result['menit']} menit - {detik_result['detik']} detik")