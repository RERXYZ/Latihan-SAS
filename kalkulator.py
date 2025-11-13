print("----KALKULATOR SEDERHANA---")
a1 = input("Masukkan angka pertama:")
b1 = input("Masukkan angka kedua:")
a = int(a1)
b = int(b1)
print("---Operasi Matematika---")
OperasiMatematika = ["1. Penjumlahan", "2. Pengurangan", "3. Perkalian", "4. Pembagian", "5. Modulus"]
for operasi in OperasiMatematika:
    print(operasi)
operator = input("Pilih operasi (tulis angkanya saja, contoh: 1):")

if operator == "1":
    print("Hasil =", a + b)
elif operator == "2":
    print("Hasil =", a - b)
elif operator == "3":
    print("Hasil =", a * b)
elif operator == "4":
    print("Hasil =", a//b)
else:
    print("Hasil =", a%b)
