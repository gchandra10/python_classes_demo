## Composition Example

## Composition Relationship : HAS A

## Car HAS A Engine
## Computer HAS A CPU
## Computer HAS A Memory



class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower
    
    def start(self):
        return "Engine with horsepower {} starts".format(self.horsepower)

class Car:
    def __init__(self, make, model, horsepower):
        self.make = make
        self.model = model
        self.engine = Engine(horsepower)  # Composition relationship
    
    def start(self):
        return "The {} {} starts: {}".format(self.make, self.model, self.engine.start())

# Example usage
my_car = Car("Toyota", "Corolla", 132)
print(my_car)
print(my_car.start())

###

class CPU:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

class Memory:
    def __init__(self, size):
        self.size = size  # In GB

class Storage:
    def __init__(self, type, capacity):
        self.type = type  # SSD or HDD
        self.capacity = capacity  # In GB

class Computer:
    def __init__(self, cpu_brand, cpu_model, mem_size, storage_type, storage_capacity):
        self.cpu = CPU(cpu_brand, cpu_model)
        self.memory = Memory(mem_size)
        self.storage = Storage(storage_type, storage_capacity)
        
    def __str__(self):
        return (f"My computer has {self.cpu.brand}, {self.cpu.model}, {self.memory.size}, {self.storage.type}, {self.storage.capacity}")

# Usage
my_computer = Computer("Intel", "i7", 16, "SSD", 512)

print(my_computer)