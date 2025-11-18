from abc import ABC, abstractmethod

class TeamF1(ABC): #Abstraksi
    total_team = 0
    musim = "2025"

    def __init__(self, nama_team, asal_team): #Enkapsulasi dan Dunder method
        self._nama_team = nama_team
        self._asal_team = asal_team
        self._driver = []
        TeamF1.total_team += 1

    @abstractmethod
    def info_team(self):
        pass

    def tambah_driver(self,driver): #Instance method
        self._driver.append(driver)

    @classmethod #Class method
    def get_total_team(cls):
        return cls.total_team
    
    @staticmethod #Static method
    def format_nama_driver(nama):
        "mengformat nama driver menjadi uppercase"
        return nama.upper()
    

class MercedesEngine(TeamF1): #Pewarisan
    def info_team(self):
        return f"Mesin Mercedes: {self._nama_team} dari {self._asal_team} - Driver: {self._driver}"
    
class FerrariEngine(TeamF1): #Polimorfisme
    def info_team(self):
        return f"Mesin Ferrari: {self._nama_team} dari {self._asal_team} - Driver: {self._driver}"

class HondaEngine(TeamF1): #Polimorfisme
    def info_team(self):
        return f"Mesin Honda: {self._nama_team} dari {self._asal_team} - Driver: {self._driver}"



#Membuat objek
Mercedes = MercedesEngine("Mercedes-AMG","Inggris")
Mercedes.tambah_driver("George Russel")
Mercedes.tambah_driver("Kimi Antonelli")

Ferrari = FerrariEngine("Scuderia Ferrari","Italia")
Ferrari.tambah_driver("Charles Leclerc")
Ferrari.tambah_driver("Lewis Hamilton")

Redbull = HondaEngine("Redbull Racing","Austria")
Redbull.tambah_driver("Max Verstappen")
Redbull.tambah_driver("Yuki Tsunoda")

Mclaren = MercedesEngine("Mclaren","Inggris")
Mclaren.tambah_driver("Lando Norris")
Mclaren.tambah_driver("Oscar Piastri")


print(f"Formula 1 Musim {TeamF1.musim}\n")
print("Daftar Team Formula 1: ")

team_list = [Mercedes, Ferrari, Redbull, Mclaren]

for team in team_list:
    print(f"- {team.info_team()}")

print(f"Total Team: {TeamF1.get_total_team()} team")
print(f"Musim: {TeamF1.musim}")
