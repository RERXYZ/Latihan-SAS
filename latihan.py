# Membuat class Mahasiswa (Blueprint / cetakan objek)
class Mahasiswa:
    # Constructor → otomatis jalan saat objek dibuat
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Method untuk menampilkan data
    def tampilkan_info(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print("----------------------")

    # Method untuk mengubah jurusan
    def ganti_jurusan(self, jurusan_baru):
        self.jurusan = jurusan_baru


# Membuat objek dari class Mahasiswa
print ("Sebelum jurusan diubah:")
mhs1 = Mahasiswa("Andi", "23051234", "Teknik Komputer")
#mhs2 = Mahasiswa("Siti", "23053211", "Sistem Informasi")

# Menampilkan info mahasiswa
mhs1.tampilkan_info()
#mhs2.tampilkan_info()

# Mengubah jurusan salah satu mahasiswa
mhs1.ganti_jurusan("Teknik Informatika")

# Menampilkan info setelah diubah
print("Setelah jurusan diubah:")
mhs1.tampilkan_info()
