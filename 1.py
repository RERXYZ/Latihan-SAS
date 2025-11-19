from abc import ABC, abstractmethod

class Hewan(ABC):
    nama = "Hewan"

    def __init__(self, jenis, umur):
        self._jenis = jenis
        self.__umur = umur

    @abstractmethod
    def suara(self):
        pass

    def info(self):
        return f"{self.nama} adalah seekor {self._jenis} berumur {self.__umur} tahun"

    @classmethod
    def kategori(cls):
        return "Makhluk hidup dari kingdom Animalia"

    @staticmethod
    def makan():
        return "Hewan butuh makan agar tetap hidup"


class Kucing(Hewan):
    def __init__(self, umur):
        super().__init__("Kucing", umur)
        self.nama = "Kucing Imut"

    def suara(self):
        return "Meow meow~"


class Anjing(Hewan):
        def __init__(self, umur):
            super().__init__("Anjing", umur)
            self.nama = "Anjing Ceria"

        def suara(self):
            return "Guk guk!"


class Burung(Hewan):
    def __init__(self, umur):
        super().__init__("Burung", umur)
        self.nama = "Burung Kicau"

    def suara(self):
        return "Cuit cuit~"


def main():
    hewan_list = [
        Kucing(2),
        Anjing(4),
        Burung(1)
    ]

    print("\n=== DATA HEWAN DI KEBUN BINATANG ===\n")

    for h in hewan_list:
        print(h.info())
        print("Suara:", h.suara())
        print("----------------------------")

    print("\n=== METHOD LAIN ===")
    print("Kategori:", Hewan.kategori())
    print("Makan:", Hewan.makan())


if __name__ == "__main__":
    main()
