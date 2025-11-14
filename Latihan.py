# def check_number(angka):
#     if angka == 0:
#         print(f"{angka} adalah nol")
#     elif angka > 0:
#         print(f"{angka} adalah positif")
#     else:
#         print(f"{angka} adalah negatif")
    
# check_number(int(input("masukan angka: ")))


###################################################################

# def count_even(angka):

#     total = 0
#     for i in angka:
#         if i % 2 == 0:
#             total += 1

#     print(f"Jumalah bilangan genap: {total}")
# data =[]
# while True:

#     print(f"""
#         1.tambah bilangan
#         2.hitung bilangan genap
#         3.keluar
# """)
#     inputan = input("Pilih menu(1/2/3): ")
    
#     print(f"isi list: {data}")
#     match inputan:
#         case "1":
#             data.append(int(input("masukan bilangan: ")))
#         case "2":
#             count_even(data)
#         case "3":
#             print("terima kasih telah menggunakan program ini")
#             break



################################################################################

# def total_harga(data):
#     total = 0
#     for i in data.values():
#         total += i

#     print(f"list baramg: {data}")
#     print(f"Total harga: Rp.{total}.00")


# masukan = {}
# while True:
#     barang = input("masukan nama barang (ketik 'selesai' untuk berhenti dan ketik 'cek' untuk mengecek total harga): ")
#     if barang.lower() == 'selesai':
#         break
#     elif barang.lower() == 'cek':
#         total_harga(masukan)
#         continue
#     harga = int(input(f"masukan harga {barang}: "))
#     masukan[barang] = harga

################################################################



# def cek_barang(gudang, nama_barang):
#     if nama_barang in gudang:
#         value = gudang[nama_barang]
#         print(f"Barang tersedia, stok: {value}")
#     else:
#         print("Barang tidak ditemukan")

# gudang = {"nasi": 10, "mie": 5, "teh": 8}
# cek = input("masukan nama barang yang ingin di cek: ")
# cek_barang(gudang, cek)


#####################################################################################


def coount_characters(s):
    total_dictionary = {}
    
    for i in s:
        if i in total_dictionary:
            total_dictionary[i] += 1
        else:
            total_dictionary[i] = 1
    print(f"jumlah karakter: {total_dictionary}")

masukan = input("masukan kalimat: ")
coount_characters(masukan)

