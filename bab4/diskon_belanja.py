total = int(input('masukan total: '))

if(total >= 500000):
    diskon = 0.2
else: 
    if(total >= 200000):
       diskon = 0.1 
    else :
        diskon = 0

bayar = total - (total * diskon)
print("total : Rp", total)
print("diskon :", diskon * 100,"%")
print("bayar : Rp", bayar)
