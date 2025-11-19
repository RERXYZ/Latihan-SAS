from abc import ABC, abstractmethod

class Bentuk(ABC): 
    dimensi = "Bangun Datar" #variabel kelas
    def __init__(self, nama, jumlah_sisi, warna = "putih"):
        self.__nama = nama #private variabel
        self.jumlah_sisi = jumlah_sisi #variabel instance
        self.__warna = warna
    def get_nama(self):
        return self.__nama
    def __str__(self): #spesial method
        return f"Bentuk: {self.__nama}, Sisi: {self.jumlah_sisi}"
    
    @classmethod
    def create_default(cls):
        return persegi(4.5, warna = "biru")
    
    @staticmethod
    def info_dimensi():
        return "semua bentuk disini termasuk bentuk 2 dimensi"
    
    @abstractmethod #abstraction
    def luas(self):
        pass

class persegi(Bentuk): #inheritance (persegi mewarisi bentuk)
    def __init__(self,sisi):
        super().__init__("persegi", 4)
        self.__sisi = sisi #private variabel
        self.jumlah_sisi = 4 #variabel instance
    def luas(self): #polimorfisme
        return self.__sisi * self.__sisi
    def keliling(self): #instance method
        return 4 * self.__sisi
    
class segitiga(Bentuk): #inheritance (segitiga mewarisi bentuk)
    def __init__(self, alas, tinggi, total_sudut = 180):
        super().__init__("segitiga", 3)
        self.__alas = alas #private variabel
        self.__tinggi = tinggi #private variabel
        self.jumlah_sisi = 3
    def luas(self):
        return (self.__alas * self.__tinggi) * 0.5
    
p1 = persegi(4) #objek1
p2 = segitiga(5,2) #objek2

print(p1.luas())
print(p1.keliling())
print(p2.luas())
