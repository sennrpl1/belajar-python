berat = int(input("masukan berat badan anda (kg):  "))
tinggi = float(input("masukan tinggi badan anda:  "))

bmi = berat / ((tinggi/100)**2)

if (bmi < 18.5) :
    kategori = "kurus (underweight)"
    keterangan = "perlu tambah berat badan"
elif (bmi <24.9) :
    kategori = "normal (ideal)"
    keterangan = "pertahankan gaya hidup mu"
elif (bmi <29.9) :
    kategori = "gemuk (overwoight)"
else :
    kategori = "obesitas"
    keterangan = "konsultasi dokter"

print("nilai bmi : ", bmi)
print("kategori :", kategori)
print("keterangan :", keterangan)