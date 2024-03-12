def perkalian(x, y):
    hasil = 0
    for i in range(y):
        hasil += x
    return hasil

# Contoh penggunaan fungsi perkalian()
hitung = [(6, 5), (7, 10)]
for x, y in hitung:
    hasil = perkalian(x, y)
    print(f"{x}x{y}=", end="")
    for i in range(y):
        if i != y - 1:
            print(f"{x}+", end="")
        else:
            print(f"{x}={hasil}.")
