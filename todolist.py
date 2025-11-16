todo = []

while True:
    tugas = input("Masukkan tugas (atau ketik 'lihat' untuk melihat daftar, 'stop' untuk keluar): ")

    if tugas == "lihat":
        print("\nDaftar Tugas:")
        for t in todo:
            print("-", t)
        print()
    elif tugas == "stop":
        print("Program selesai.")
        break
    else:
        todo.append(tugas)
        print("Tugas ditambahkan!")
