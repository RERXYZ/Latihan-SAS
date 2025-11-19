from abc import ABC, abstractmethod


#Abstraction

class Item(ABC):
    def __init__(self, title, year):
        self._title = title        # protected (encapsulation)
        self.__year = year         # private (encapsulation)
    
    @abstractmethod
    def info(self):
        pass

    def get_year(self):            # getter
        return self.__year

    def set_year(self, year):      # setter
        if year > 0:
            self.__year = year


# ==========================================
# INHERITANCE dari Item
# Polymorphism implemented di method info()
# ==========================================
class Book(Item):
    total_books = 0  # class variable

    def __init__(self, title, year, author):
        super().__init__(title, year)
        self.author = author       # instance variable
        Book.total_books += 1

    def info(self):  # Polymorphism
        return f"Buku: {self._title} ({self.get_year()}) oleh {self.author}"

    @classmethod
    def get_total_books(cls):  # class method
        return cls.total_books

    @staticmethod
    def library_rules():  # static method
        return "Buku harus dikembalikan maksimal 7 hari."


class Magazine(Item):
    def __init__(self, title, year, month):
        super().__init__(title, year)
        self.month = month

    def info(self):  # Polymorphism
        return f"Majalah: {self._title} - Edisi {self.month} {self.get_year()}"



# CLASS PERPUSTAKAAN 
class Library:
    def __init__(self):
        self.collection = []  # instance variable

    def add_item(self, item):  # instance method
        self.collection.append(item)

    def show_all_items(self):
        for item in self.collection:
            print(item.info())  # polymorphism in action



# MAIN PROGRAM
book1 = Book("Pemrograman Python", 2020, "Budi")
book2 = Book("Algoritma Dasar", 2019, "Siti")

mag1 = Magazine("Tekno Harian", 2024, "Januari")

library = Library()
library.add_item(book1)
library.add_item(book2)
library.add_item(mag1)

library.show_all_items()

print("\nTotal Buku:", Book.get_total_books())
print("Peraturan:", Book.library_rules())
