from abc import ABC, abstractmethod
class hewan(ABC):
    pass
class Kucing(hewan):
    def suara(self):
        return "Meong"
class Anjing(hewan):
    def suara(self):
        return "Guk Guk"
    def buat_suara(hewan):
        print(hewan.suara())
    buat_suara(Kucing())