from abc import ABC, abstractmethod

# ===============================
# Abstraction
# ===============================
class hewan(ABC):
    def __init__(self, nama):
        # Encapsulation: private variable
        self.__nama = nama

    # Getter & Setter untuk name
    def get_nama(self):
        return self.__nama

    def set_name(self, nama):
        self.__nama = nama

    # Abstract method
    @abstractmethod
    def sound(self):
        pass

    # Method untuk add (menggabungkan nama hewan)
    def __add__(self, other):
        if isinstance(other, hewan):
            return f"{self.__nama} + {other.get_nama()}"
        return NotImplemented


# ===============================
# Inheritance & Polymorphism
# ===============================
class anjing(hewan):
    def sound(self):
        print(f"{self.get_nama()} berkata: Woof!")


class kucing(hewan):
    def sound(self):
        print(f"{self.get_nama()} berkata: Meow!")


# ===============================
# Penggunaan program
# ===============================
if __name__ == "__main__":
    dog = anjing("Ikar")
    cat = kucing("Jamal")

    # Polymorphism: method sound berbeda
    dog.sound()
    cat.sound()

    # Encapsulion: akses nama melalui getter
    print(dog.get_nama())
    dog.set_name("Wuli")
    print(dog.get_nama())

    # Operator overloading (+) dengan str
    combined = dog + cat
    print("Hasil penjumlahan nama hewan:", combined)
