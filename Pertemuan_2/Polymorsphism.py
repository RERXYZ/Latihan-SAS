class Kucing:
    def suara(self):
        return "Meong"
class Anjing:
    def suara(self):
        return "Guk Guk"
    def buat_suara(hewan):
        print(hewan.suara())
    buat_suara(Kucing())
    buat_suara(Anjing())