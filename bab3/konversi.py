# kalkulator konversi satuan
print("=== KALKULATOR KONVERSI ===")
cm = float(input ("masukkan panjang (cm) : "))

# konversi ke berbagai satuan
meter = cm / 100
km = cm / 100000
inci = cm / 2.54
kaki = inci / 12

print()
print(cm, "cm =", meter, "meter")
print(cm, "cm =", km, "kilometer")
print(cm, "cm =", round(inci, 2), "inci")
print(cm, "cm =", round(kaki, 2), "kaki")
