# program penentu kelulusan smk tjp tuban
print("=" * 40)
print(" SISTEM PENILAIAN SISWA")
print("=" * 40)
nama       = input("nama siswa    : ")
nilai_uts  = float(input("nilai uts (0 - 100):"))
nilai_uas  = float(input("nilai uas (0 - 100):"))
niali_tugas= float(input("nilai tugas        :"))

#hitung rata-rata
rata = (nilai_uts * 0.3) + (nilai_uas * 0.5) + (niali_tugas * 0.2)

#tentukan kategori
if rata >= 90:
    predikat = "A - sangat baik"
elif rata >= 80:
    predikat = "B - baik"
elif rata >= 70:
    predikat = "C - cukup"
elif rata >= 60:
    predikat = "D - kurang"
else:
    predikat = "E - sangat kurang"

lulus = rata >= 70

print()
print("=" * 40)
print("  HASIL PENILAIAN")
print("=" * 40)
print("NAMA     :", nama)
print("rata-rata:", round(rata, 21))
print("predikat :", predikat)
print("status   :", "LULUS" if lulus else "TIDAK LULUS")