from modules.cars import *

'''If importing everything, must define the * in a file called __init__ with __all__ and the name of the modules.
Create the file inside a module
'''
bmw = car.Car("bmw", "black", 2017)

print(bmw.year_of_making())

print(bmw.__repr__)

def get_install_requirements():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        reqs = [x.strip() for x in f.read().splitlines()]
    reqs = [x for x in reqs if not x.startswith("#")]
    print(reqs)


get_install_requirements()



