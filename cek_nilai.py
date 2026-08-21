# program cek kondisi nilai
nama = input ('nama siswa :')
nilai = int (input('nilai ujian : '))
hadir = input ('hadir 80%? (ya/tidak): ')

# operator perbandingan
print ()
print ('=== hasil cek===')
print ('nilai>= 75 :', nilai >= 75)
print ('nilai >= 90 :', nilai >= 90)
print ('nilai antara 75-89:', nilai >= 75 and nilai <= 89)

#operator logika
hadir_ok = hadir == "ya"
lulus = nilai >= 75 and hadir_ok
remedial = nilai <75 or not hadir_ok

print ("lulus       :", lulus)
print ("perlu remedial:", remedial)