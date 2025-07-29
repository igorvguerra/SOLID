class Animal:
    def eat(self):
        print("The animal is eating.")

    def poop(self):
        print("The animal is pooping.")


class Bird(Animal):
    def fly(self):
        print("The bird is flying")

class Dove(Bird):
    def walk(self):
        print("The dove is walking")

class Person:
    def watching(self, animal: Animal):
        animal.eat()


animal = Animal()
bird = Bird()
dove = Dove()
person = Person()

animal.eat()
bird.eat()
dove.eat()
person.watching(animal)
person.watching(bird)
person.watching(dove)