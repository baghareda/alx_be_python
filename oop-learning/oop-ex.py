class Person:
    def __init__(self, name, age):
        self.age = age
        self.name = name
        
    def __del__(self):
        print(f"farewell deleted his name {self.name} and his age is: {self.age}")
        
p = Person("Reda", 25)
del p
        