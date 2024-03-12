def ganjil(bts_bawah, bts_atas):
    if bts_bawah < bts_atas:
        deret_bil_ganjil = [i for i in range(bts_bawah, bts_atas+1) if i % 2 != 0]
    else:
        deret_bil_ganjil = [i for i in range(bts_bawah, bts_atas-1, -1) if i % 2 != 0]
    return deret_bil_ganjil

bts_bawah = 10
bts_atas = 30

hasil = ganjil(bts_bawah, bts_atas)
if bts_bawah < bts_atas:
    print("bawah =", bts_bawah, ", atas =", bts_atas, ". Karena bawah < atas, berarti dari kecil ke besar, maka hasilnya")
else:
    print("bawah =", bts_bawah, ", atas =", bts_atas, ". Karena bawah > atas, berarti dari besar ke kecil, maka hasilnya")

print("adalah:", end=" ")
for i in range(len(hasil)):
    if i == len(hasil) - 1:
        print(hasil[i], end="")
    else:
        print(hasil[i], end=", ")