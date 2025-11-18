from abc import ABC, abstractmethod
class buku(ABC):
    jenis ="komik"
    def __init__(self, judul, pengarang, tahun_terbit, harga):
        self.judul=judul
        self.pengarang=pengarang
        self.tahun_terbit=tahun_terbit
        self._harga=harga
    def get_harga(self):
        return self._harga
    def set_harga(self, harga_baru):
         if harga_baru>0:
             self.harga=harga_baru
    def tampilkan_info(self):
        print(f"Judul                : {self.judul}")
        print(f"Pengarang            : {self.pengarang}")
        print(f"Tahun Tebit          : {self.tahun_terbit}")
        print(f"Jenis Buku           : {buku.jenis}")
        print(f"Harga                : {self.harga}")