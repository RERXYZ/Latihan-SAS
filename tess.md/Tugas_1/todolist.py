def to_do_list():
    aktivitass =[]
    while True:
        print ("1. Tambahkan aktivitas")
        print ("2. Hapus Aktivitas")
        print ("3. Tunjukan aktivitas")
        print ("4. Keluar")
        pilih = input("Masukan pilihan = ")
        if pilih == "1":
            aktivitas = input("Masukan Aktivitas :")
            aktivitass.append(aktivitas)
        elif pilih == "2":
            aktivitas=input("Pilih aktivitas yang akan dihapus")
            if aktivitas in aktivitass:
                aktivitass.remove(aktivitas)
            else:
                print("Aktivitas tidak ditemukan")
        elif pilih == "3":
            print ("Aktivitas yang ada: ")
            for aktivitas in aktivitass:
                print("- "+aktivitas)
        elif pilih == "4":
            break
        else:
            print("Pilihan tidak ada")
to_do_list()
