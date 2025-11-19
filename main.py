from abc import ABC, abstractmethod


class Mob(ABC):
    mob_count = 0

    def __init__(self, name, health):
        self._name = name
        self.__health = health
        Mob.mob_count += 1

    @property
    def health(self):
        return self.__health

    @health.setter
    def health(self, value):
        self.__health = max(0, value)
        if self.__health == 0:
            print(f"{self._name} mati.")
            Mob.mob_count -= 1

    def receive_damage(self, amount):
        self.health -= amount
        print(f"{self._name} sisa HP: {self.health}")

    @classmethod
    def get_total_mobs(cls):
        print(f"Total Mob: {cls.mob_count}")

    @staticmethod
    def check_spawn(light_level):
        return light_level < 7

    @abstractmethod
    def attack(self):
        pass


class Zombie(Mob):
    def attack(self):
        print(f"{self._name} memukul player.")


class Creeper(Mob):
    def attack(self):
        print(f"{self._name} meledak!")
        self.health = 0


if __name__ == "__main__":
    if Mob.check_spawn(5):
        zombie = Zombie("Zombie", 20)
        creeper = Creeper("Creeper", 20)

    Mob.get_total_mobs()

    mobs = [zombie, creeper]

    for mob in mobs:
        mob.attack()
        mob.receive_damage(10)
        print("-" * 10)

    Mob.get_total_mobs()