# polymorphism: is the ability of an object to take on many forms. In python, polymorphism allows
# us to define methods in the child class with the same name as defined in their parent class.


class Dog:
    def sound(self):
        print("Woof")


class Cat:
    def sound(self):
        print("Meow")


object1 = Dog()
object2 = Cat()
object1.sound()
object2.sound()
