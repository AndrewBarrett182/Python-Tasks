from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass

class Mammal(Animal):
    def eat(self):
        print("nom nom")

# Abstraction shows the structure the subclass must follow