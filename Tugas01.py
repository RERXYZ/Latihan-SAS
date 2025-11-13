##Kalkulator sederhana
# def algoritma(angka1, angka2, masukan):
#     if masukan == "1":
#         return angka1 + angka2
#     elif masukan == "2":
#         return angka1 - angka2
#     elif masukan == "3":
#         return angka1 * angka1
#     else:
#         return angka1 / angka2
    

# print(f"""
# 1.penjumlahan
# 2.pengurangan
# 3.perkalian
# 4.pembagian
# """)
# angka1 = int(input("masukan angka pertama: "))
# operasi = input("operasi apa yang mau dipilih(1/2/3/4): ")
# angka2 = int(input("masukan angka ke 2: "))

# match operasi:
#     case "1":
#         masukan = '+'
#     case "2":
#         masukan = '-'
#     case "3":
#         masukan = 'X'
#     case "4":
#         masukan = '/'

# hasil = algoritma(angka1, angka2, operasi)

# if operasi == "4":
#     print(f"hasil dari {angka1} {masukan} {angka2} adalah: {hasil:.2f}")
# else:
#     print(f"hasil dari {angka1} {masukan} {angka2} adalah: {hasil}")    


##To Do List

tugas = []

def tampilkan():
    if not tugas:
        print("belum ada tugas")
        print('=' * 20)
        print()
    else:

        print("List tugas anda")
        print()
        for i in tugas:
            print(i)
        print('=' * 20)
        print()


def tambah():
    tugas.append(input("masukan tugas: "))
    print("Tugas berhasil ditambahkan")
    print('=' * 20)
    print()

def hapus():
    tampilkan()
    adalah = input("tugas mana yang mau di hapus: ")
    tugas.remove(adalah)
    print(f"{adalah} telah terhapus")
    print('=' * 20)
    print()


while True:
    print(f"""
        1.tampilkan tugas
        2.tambah tugas
        3.hapus tugas
        4.berhenti
    """)
    masukan = input("mau melakukan apa?: ")

    match masukan:
        case "1":
            tampilkan()
        case "2":
            tambah()
        case "3":
            hapus()
        case "4":
            print("program berhenti")
            break

    