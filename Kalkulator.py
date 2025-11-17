def tambah(x, y):
    return x + y

def kurang(x, y):
    return x - y

def kali(x, y):
    return x * y

def bagi(x, y):
    if y == 0:
        return "Error! Pembagian dengan nol tidak diizinkan."
    return x / y
print ("Pilih Operasi.\n1. Tambah (+)\n2. Kurang (-)\n3. Kali (*)\n4. Bagi (/)\n5. Keluar\n" + "-" * 20)

while True:
    pilihan = input("Masukkan pilihan (1/2/3/4/5): ")

    if pilihan in ('1','2','3','4'):
        try:
            angka1 = float(input("Masukkan angka pertama: "))
            angka2 = float(input("Masukkan angka kedua: "))
        except ValueError:
            print("Input tidak valid. Harap masukkan angka.")
            continue
        if pilihan == '1':
            print(f"{angka1} + {angka2} = {tambah(angka1, angka2)}")  
        elif pilihan == '2':
            print(f"{angka1} - {angka2} = {kurang(angka1, angka2)}")
        elif pilihan == '3':
            print(f"{angka1} * {angka2} = {kali(angka1, angka2)}")
        elif pilihan == '4':
            hasil_bagi = bagi(angka1, angka2)
            print(f"{angka1} / {angka2} = {hasil_bagi}")
        print("-" * 20)
    elif pilihan == '5':
        print("Terima kasih telah menggunakan kalkulator!")
        break
    else:
        print("Pilihan tidak valid. Silakan coba lagi.")
        print("-" * 20)
    
