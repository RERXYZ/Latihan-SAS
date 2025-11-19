from abc import ABC, abstractmethod

# dis abc cls anm
class Animal(ABC):
    def __init__(self, name):
        self.__name = name  # dis enc atr prv
    
    @abstractmethod
    def speak(self):
        pass
    
    def get_name(self): 
        return self.__name


# inh dog fr anm
class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.__breed = breed
    
    # pol ovr abs mth
    def speak(self):
        return f"{self.get_name()} barks: Woof!"
    
    def get_breed(self):
        return self.__breed


# same
class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.__color = color
    
    # same
    def speak(self):
        return f"{self.get_name()} meows: Meow!"
    
    def get_color(self):
        return self.__color


# same as main() but only for oop
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    cat = Cat("Whiskers", "Orange")
    
    print(dog.speak())
    print(f"Breed: {dog.get_breed()}\n")
    
    print(cat.speak())
    print(f"Color: {cat.get_color()}")