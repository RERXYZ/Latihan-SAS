# Kalkulator sederhana

print("Kalkulator Sederhana")

# Input angka pertama
num1 = float(input("Masukkan angka pertama: "))

# Input angka kedua
num2 = float(input("Masukkan angka kedua: "))

# Pilihan operasi
print("Pilih operasi:")
print("1. Penjumlahan (+)")
print("2. Pengurangan (-)")
print("3. Perkalian (*)")
print("4. Pembagian (/)")

# Input pilihan operasi
operasi = input("Masukkan pilihan (1/2/3/4): ")

# Melakukan operasi sesuai pilihan
if operasi == '1':
    print(f"{num1} + {num2} = {num1 + num2}")
elif operasi == '2':
    print(f"{num1} - {num2} = {num1 - num2}")
elif operasi == '3':
    print(f"{num1} * {num2} = {num1 * num2}")
elif operasi == '4':
    if num2 != 0:
        print(f"{num1} / {num2} = {num1 / num2}")
    else:
        print("Error! Pembagi tidak boleh nol.")
else:
    print("Pilihan tidak valid!")
