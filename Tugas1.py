#Tegar Computer - Bojongsoang Electronic Center

from abc import ABC, abstractmethod   #abstrak

class Perangkat(ABC): #inherit kelas ABC nya dari import ABC, Abstrac Base Class
    @abstractmethod
    def info(self):
        pass #biar tidak error dan skip kebawah

class Laptop(Perangkat): #yang mewarisi
    def __init__(self, merk, ram, harga):
        self.merk = merk  #public
        self._ram = ram   #protected  (cuman satu)
        self.__harga = harga #private (doublespasi)

    def getHarga(self): #polimorfisme
        return self.__harga #ini private, ambil harga di private

    def setHarga(self, harga_baru):
        if harga_baru > 0:   #biar gk negatif, kalau dibawah 0 ada -1, -2
            self.__harga = harga_baru

    def info(self): 
        print(f"Laptop {self.merk} | RAM {self._ram}GB | Harga Rp{self.__harga}")


class GamingLaptop(Laptop): #laptop sebagai inheritance
    def __init__(self, merk, ram, harga, gpu):
        super().__init__(merk, ram, harga)
        self.gpu = gpu

    def info(self):
        print(f"Laptop Gaming {self.merk} | RAM {self._ram}GB | GPU {self.gpu} | Harga Rp{self.getHarga()}")


l1 = Laptop("Lenovo", 8, 6500000)
l2 = GamingLaptop("Asus ROG", 16, 20000000, "RTX 4060")

l1.info()
l2.info()

print("\nHarga lama standar laptop:", l1.getHarga())
l1.setHarga(7000000)
print("Harga baru standar laptop:", l1.getHarga())

print("\nHarga lama gaming laptop:", l2.getHarga())
l2.setHarga(30000000)
print("Harga baru gaming laptop:", l2.getHarga())