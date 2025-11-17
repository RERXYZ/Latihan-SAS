# penjelasan abstraksi dalam oop
# Menyederhanakan kompleksitas dengan hanya menampilkan fitur penting, dan menyembunyikan detail implementasinya.

from abc import ABC, abstractmethod

# Kelas abstrak
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass   # hanya deklarasi, tanpa implementasi

    @abstractmethod
    def perimeter(self):
        pass

# Kelas konkret yang mengimplementasikan abstraksi
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Kelas lain yang juga mengimplementasikan abstraksi
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius

    def perimeter(self):
        return 2 * 3.14 * self.radius


# Contoh penggunaan
shapes = [
    Rectangle(4, 5),
    Circle(3)
]

for s in shapes:
    print("Area:", s.area())
    print("Perimeter:", s.perimeter())