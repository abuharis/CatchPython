'''
Decorators are useful feature to avoid repetition of codes in python. It is called as Cross-cutting concerns.
Cross-cutting concerns are parts of a program that rely on or must affect many other parts of the system.
'''


'''The dataclass contains init, repr eq and so many general methods part of python module.'''
#https://peps.python.org/pep-0557/


from dataclasses import dataclass
from classes.magic_methods import magic


@dataclass
class Human:
    name: str
    gender: bool

    """The __repr__ calls automatically when the class is invoked"""
    def __repr__(self):
        """Return a string representation of the project"""
        return f"The name is {self.name} and {self.gender}"

messi = Human("messi", 1)
ronaldo = Human("Christiano", 1)
print(messi.__repr__())

int.__add__()

print(messi)
print(ronaldo)

print(messi == ronaldo)


@dataclass
class Car:
    name: str
    price: int


bmw = Car("black", 44)
audi = Car("black", 44)

print(bmw.__repr__)     #This gives the format representation according to the dataclass
print(Car.__eq__(bmw, audi))        #Equating objects parameters