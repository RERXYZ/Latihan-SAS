# penjelasan inheritance dalam oop
# Kemampuan suatu class untuk mewarisi atribut dan metode dari class lain

class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def start_engine(self):
        return "Engine started"

class Car(Vehicle):
    def __init__(self, make, model, num_doors):
        super().__init__(make, model)
        self.num_doors = num_doors

    def honk(self):
        return "Beep beep!"
    
# penggunaan inheritance
car = Car("Toyota", "Corolla", 4)
print(car.start_engine())      # Output: Engine started
print(car.honk())              # Output: Beep beep!