#Calculator by Andreas Tegar Bagaskoro
#102022500150
#S1 Sistem Informasi

perkenalan = "Selamat Datang di Tugas Kalkulator Sederhana - Coridor Programmming Robotic SAS 2025"
print(perkenalan)

pilihoperasi = input("Pilih Operator Perhitungan (tambah, kurang, kali, bagi, pangkat): ")
bilangan1 = int(input("Masukkan Bilangan Pertama: "))
bilangan2 = int(input("Masukkan Bilangan Kedua: "))

if pilihoperasi == "tambah":
   hasilgokil = bilangan1 + bilangan2
   print("Hasil Penjumlahan: ")
   print(int(hasilgokil))

elif pilihoperasi == "kurang":
   hasilgokil = bilangan1 - bilangan2
   print("Hasil Pengurangan: ")
   print(int(hasilgokil))

elif pilihoperasi == "kali":
   hasilgokil = bilangan1 * bilangan2
   print("Hasil Perkalian: ")
   print(int(hasilgokil))

elif pilihoperasi == "bagi":
   hasilgokil = bilangan1 / bilangan2
   print("Hasil Pembagian: ")
   print(int(hasilgokil))

elif pilihoperasi == "pangkat":
   hasilgokil = bilangan1 ** bilangan2
   print("Hasil Perpangkatan: ")
   print(int(hasilgokil))

else:
   print(f"{pilihoperasi} tidak valid, silahkan pilih operator yang valid.")