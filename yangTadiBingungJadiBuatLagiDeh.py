###OOP BIKIN MUMET
from abc import ABC,abstractmethod


class mobil(ABC):

    @abstractmethod
    def info_mobil(self):       #<-- abstaction
        pass

class jualMobil(mobil):

    nama_pt = "PT. semoga barokah"

    #enkapulasi 
    def __init__(self, merek, tahun, cc, harga):   

        self.merek = merek
        self.tahun = tahun
        self._cc = cc #<--protected
        self.__harga = harga #<--privatae        #<--variabel instance

    #getter
    def get_harga(self):
        return self.__harga
    

    def ganti_harga(self, harga_baru):
        self.__harga = harga_baru

    #instance method
    def info_mobil(self):
        print()
        print("{}\n{}\ntahun: {}\ncc: {}\nharga: {}".format(
            jualMobil.nama_pt,
            self.merek,
            self.tahun,
            self._cc,
            self.get_harga()

        ))


    def __str__(self):
        return f"jualMobil(merek: {self.merek})"
    
    @classmethod
    def ubahNamaPT(cls, nama_baru):
        cls.nama_pt = nama_baru

    @staticmethod
    def sapaan():
        return "selamat datang"


#pewarisan
class mobilmahal(jualMobil):
    def __init__(self, merek, tahun, cc, harga, turbo):
        super().__init__(merek, tahun, cc, harga)
        self.turbo = turbo

        if self.turbo:
            self.turbo = "ADA"
        else:
            self.turbo = "TIDAK ADA"

    def info_mobil(self):
        print()
        print("{}\nMobil mewah nih bos\n{}\ntahun: {}\ncc: {}\nharga: {}\nturbo: {}".format(
            jualMobil.nama_pt,
            self.merek,
            self.tahun,
            self._cc,
            self.get_harga(),
            self.turbo
        ))
        
print(jualMobil.sapaan())



mobil_biasa = jualMobil("toyota", 2010, 600, 100_000_000)
mobil_sport = mobilmahal("MCLaren", 2020, 2500, 15_000_000_000, True)

print(mobil_biasa)
print(mobil_sport)      #<--dunder method



mobil_biasa.info_mobil()
mobil_sport.info_mobil()
        

jualMobil.ubahNamaPT("PT. yang tadi bangkrut")
mobil_biasa.ganti_harga(70_000_000)
mobil_biasa.info_mobil()