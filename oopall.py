from abc import ABC, abstractmethod

class Kendaraan(ABC):

    jenis = "Transportasi"             # class variable

    def __init__(self, nama, kecepatan):
        self.nama = nama               # instance variable
        self.__kecepatan = kecepatan   # private variable

    @abstractmethod
    def info(self):
        pass

    def lihat_kecepatan(self):
        return self.__kecepatan

    def ubah_kecepatan(self, baru):
        self.__kecepatan = baru

class Mobil(Kendaraan):

    def info(self):
        print(f"{self.nama} melaju {self.lihat_kecepatan()} km/jam")

class Motor(Kendaraan):

    def info(self):
        print(f"{self.nama} melaju {self.lihat_kecepatan()} km/jam")

class Utilitas:

    @staticmethod
    def garis():
        print("-" * 30)

    @classmethod
    def deskripsi(cls):
        print("Ini adalah class utilitas")

def main():
    m1 = Mobil("Avanza", 80)
    m2 = Motor("Vario", 60)

    m1.info()
    m2.info()

    Utilitas.garis()
    Utilitas.deskripsi()

if __name__ == "__main__":
    main()