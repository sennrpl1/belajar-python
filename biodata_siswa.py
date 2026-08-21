# program biodata siswa
print('=' * 35)
print(' FORM BIODATA SISWA')
print('=' * 35)

nama = input("NAMA LENGKAP  : ")
kelas = input("KELAS       : ")
umur = int(input ("UMUR (TAHUN) :"))
tinggi = float (input ("TINGGI (cm) :"))

print()
print("=" * 35)
print(" data tersimpan")
print("=" * 35)
print("nama :", nama )
print('kelas :', kelas)
print('umur :', umur, "tahun")
print('tinggi :', tinggi, "cm")
print("sudah dewasa :", umur >=17)