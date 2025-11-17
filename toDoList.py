tugas = []
def tambahTugas():
    task = input("Masukkan tugas: ")
    tugas.append({"task": task, "done": False})
    print(f"Tugas '{task}' berhasil ditambahkan!\n")

def lihatTugas():
    if not tugas:
        print("Belum ada tugas!\n")
        return
    print("\nDaftar Tugas Anda:")
    for i, todo in enumerate(tugas, 1):
        status = "✓" if todo["done"] else "○"
        print(f"{i}. [{status}] {todo['task']}")
    print()

def tandaiSelesai():
    lihatTugas()
    try:
        num = int(input("Masukkan nomor tugas untuk ditandai selesai: "))
        tugas[num - 1]["done"] = True
        print("Tugas berhasil ditandai selesai!\n")
    except (ValueError, IndexError):
        print("Input tidak valid!\n")

def hapusTugas():
    lihatTugas()
    try:
        num = int(input("Masukkan nomor tugas untuk dihapus: "))
        tugas.pop(num - 1)
        print("Tugas berhasil dihapus!\n")
    except (ValueError, IndexError):
        print("Input tidak valid!\n")

def main():
    while True:
        print("*** Daftar Tugas ***")
        print("1. Tambah tugas")
        print("2. Liat tugas")
        print("3. Nandain klo tugas selesai")
        print("4. Hapus tugas")
        print("5. Keluar")
        choice = input("Pilih opsi: ")
        
        if choice == "1":
            tambahTugas()
        elif choice == "2":
            lihatTugas()
        elif choice == "3":
            tandaiSelesai()
        elif choice == "4":
            hapusTugas()
        elif choice == "5":
            print("Dadah :D !")
            break
        else:
            print("Pilihan tidak valid!\n")

if __name__ == "__main__":
    main()