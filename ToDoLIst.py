todo_list = []

# tambah tugas ke dalam daftar
def tambah_tugas(tugas):
    todo_list.append(tugas)
    print(f'Tugas "{tugas}" telah ditambahkan.')
    print("\n================================\n")

# lihat semua tugas
def lihat_tugas():
    if not todo_list:
        print("Tidak ada tugas dalam daftar.")
        print("\n================================\n")
    else:
        print("Daftar Tugas:")
        for idx, tugas in enumerate(todo_list, start=1):
            print(f"{idx}. {tugas}")
        print("\n================================\n")

# hapus tugas berdasarkan index
def hapus_tugas(index):
    if 0 <= index < len(todo_list):
        tugas = todo_list.pop(index)
        print(f'Tugas "{tugas}" telah dihapus.')
        print("\n================================\n")
    else:
        print("Index tugas tidak valid.")
        print("\n================================\n")

# menu utama
def main():
    while True:
        print("\nMenu ToDoList:")
        print("1. Tambah Tugas")
        print("2. Lihat Tugas")
        print("3. Hapus Tugas")
        print("4. Keluar")
        choice = input("\nPilih menu ( 1 / 2 / 3 / 4 ): ")
        print("\n================================\n")
        if choice == '1':
            # berapa banyak tugas yang ingin ditambahkan
            num_tugas = int(input("Berapa banyak tugas yang ingin Anda tambahkan? "))
            for i in range(num_tugas):
                tugas = input(f"Masukkan tugas ke-{i+1}: ")
                tambah_tugas(tugas)
        elif choice == '2':
            lihat_tugas()
        elif choice == '3':
            lihat_tugas()
            index = int(input("Masukkan nomor tugas yang ingin dihapus: ")) - 1
            hapus_tugas(index)
        elif choice == '4':
            print("Keluar dari aplikasi ToDo List.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# main function
if __name__ == "__main__":
    main()