## Demonstrates Inheritence and Function Overriding
## Dog IS A Animal
## Cat IS A Animal
## Employee IS A Person
## Student IS A Person


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass  # This method will be overridden by subclasses


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # Call the superclass constructor to initialize the name
        self.breed = breed  # Additional attribute for Dog

    def speak(self):
        return f"{self.name} the {self.breed} says Woof!"


class Cat(Animal):
    def __init__(self, name, color):
        super().__init__(name)  # Call the superclass constructor to initialize the name
        self.color = color  # Additional attribute for Cat

    def speak(self):
        return f"{self.name} the {self.color} cat says Meow!"


# Example usage
dog = Dog("Buddy", "Golden Retriever")
cat = Cat("Whiskers", "black")

print(dog.speak())  # Output: Buddy the Golden Retriever says Woof!
print(cat.speak())  # Output: Whiskers the black cat says Meow!
