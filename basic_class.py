class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof! and its {self.age} years old")


my_dog = Dog("Buddy", 2)
your_dog = Dog("Brady", 3)

my_dog.bark()
your_dog.bark()
