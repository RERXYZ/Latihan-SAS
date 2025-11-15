while True:

    angka1=float(input("Masukan angka 1 = "))
    operasi = str(input("Masukan operasi, +,-,*,/: "))
    angka2=float(input("Masukan angka 2 = "))
    if operasi == "+":
        hasil= angka1 + angka2
        print ("Hasil pertamabahan adalah = ",hasil)
    elif operasi == "-":
        hasil= angka1-angka2
        print ("Hasil pengurangan adalah = ",hasil)
    elif operasi == "*":
        hasil = angka1 * angka2
        print ("Hasil perkalian adalah = ",hasil)
    elif operasi=="/":
        hasil = angka1/angka2
        print ("Hasil pembagian adalah = ",hasil)
    else:
        print("Opsi tidak ada")
    ulang=input("Mau berhitung lagi gaK? y/n: ")
    if ulang != "y":
        print("Program selesai. ")
        break