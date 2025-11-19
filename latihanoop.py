from abc import ABC, abstractmethod

#ABSTRACTION
class Orang(ABC):
    @abstractmethod
    def info(self):
        pass

#INHERITANCE + ENCAPSULATION
class Mahasiswa(Orang):
    def __init__(self, nama, nim, jurusan):
        self.__nama = nama        # ENCAPSULATION → private attribute
        self.__nim = nim
        self.__jurusan = jurusan

    # akses data privat
    def get_nama(self):
        return self.__nama

    def get_nim(self):
        return self.__nim

    def get_jurusan(self):
        return self.__jurusan

    # Setter (ubah data privat)
    def set_jurusan(self, jurusan_baru):
        self.__jurusan = jurusan_baru

    # POLYMORPHISM → override method info()
    def info(self):
        print("=== MAHASISWA ===")
        print(f"Nama    : {self.__nama}")
        print(f"NIM     : {self.__nim}")
        print(f"Jurusan : {self.__jurusan}")

# Kelas turunan lain untuk Polymorphism
class Dosen(Orang):
    def __init__(self, nama, matkul):
        self.__nama = nama
        self.__matkul = matkul

    # POLYMORPHISM → method info() versi dosen
    def info(self):
        print("=== DOSEN ===")
        print(f"Nama     : {self.__nama}")
        print(f"Mata Kuliah : {self.__matkul}")

# PEMBUATAN OBJEK
m1 = Mahasiswa("Andi", "23051234", "Teknik Komputer")
d1 = Dosen("Bu Sari", "Pemrograman")

# Menampilkan info
m1.info()
print()
d1.info()
