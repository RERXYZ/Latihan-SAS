schedule = {
    'monday' : [],
    'tuesday' : [],
    'wednesday' : [],
    'thursday' : [],
    'friday' : [],
    'saturday' : [],
    'sunday' : [],
}

def create(day, *todo):
    for i in todo:
        schedule[day].append(i)

def read(*days):
    if days[0] == 'semua':
        days = list(schedule.keys())

    for d in days:
        print(f"\n=== {d.upper()} ===")
        if not schedule[d]:
            print("(tidak ada jadwal)")
        else:
            for i, j in enumerate(schedule[d], start=1):
                print(f"{i}. {j}")

def find(day):
    print(f"\n=== {day.upper()} ===")
    if not schedule[day]:
        print("(tidak ada jadwal)")
    else:
        for i, j in enumerate(schedule[day], start=1):
            print(f"{i}. {j}")

def update(day, *todo):
    schedule[day] = list(todo)

def delete(day):
    schedule[day] = []

def main():
    while True:
        print("""
=== JADWAL HARIAN ===
1. Tambah todo
2. Tampilkan todo
3. Tampilakan todo tertentu
4. Update todo
5. Hapus todo
6. Keluar
""")

        choice = input("Pilih: ")

        if choice == "1":
            day = input("Hari: ").lower()
            todos = input("Todo (pisahkan dengan koma): ").split(",")
            create(day, *[t.strip() for t in todos])

        elif choice == "2":
            days = input("Hari (pisahkan dengan koma atau ketik 'semua'): ").lower().split(",")
            read(*[d.strip() for d in days])

        elif choice == "3":
            day = input("Hari: ").lower()
            find(day)

        elif choice == "4":
            day = input("Hari: ").lower()
            todos = input("Todo baru (pisahkan dengan koma): ").split(",")
            update(day, *[t.strip() for t in todos])

        elif choice == "5":
            day = input("Hari: ").lower()
            delete(day)
            print("Terhapus")

        elif choice == "6":
            print("bye!")
            break

        else:
            print("Tidak ada yang cocok!")

if __name__ == '__main__':
    main()
