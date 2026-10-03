class Animal: 
    def make_sound(self):
        print('Animal makes different sound')

class Dog(Animal):
    def make_sound(self):
        print('Dog says : Woof Woof')

class Cat(Animal):
    def make_sound(self):
        print('Cat says : Meow Meow')

my_dog = Dog()
my_dog.make_sound()
my_cat = Cat()
my_cat.make_sound()