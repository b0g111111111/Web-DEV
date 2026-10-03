from abc import ABC , abstractmethod

class Animal (ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog (Animal):
    def sound(self):
        print('Dogs say Woofs')

class Cat (Animal):
    def sound(self):
        print('Cats say Meow Meow')

dog = Dog()
cat = Cat()
dog.sound
cat.sound