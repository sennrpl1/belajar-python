# contoh: tabel perkalian 1-3
for i in range(1, 10):       # loop luar: baris
    for j in range(1, 10):   # loop dalam: kolom
        print(i, "x", j, "=", i*j)
    print() # baris kosong antar tabel