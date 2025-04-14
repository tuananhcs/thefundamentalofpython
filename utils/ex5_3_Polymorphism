from abc import ABC, abstractmethod

# Định nghĩa lớp trừu tượng
class Animal(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def make_sound(self):
        pass

# Lớp con kế thừa từ lớp trừu tượng Animal
class Dog(Animal):
    def make_sound(self):
        return "Woof!"

# Lớp con khác kế thừa từ lớp trừu tượng Animal
class Cat(Animal):
    def make_sound(self):
        return "Meow!"

# Sử dụng các lớp
dog = Dog("Buddy")
cat = Cat("Whiskers")

print(f"{dog.name} says {dog.make_sound()}")
print(f"{cat.name} says {cat.make_sound()}")