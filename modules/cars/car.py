from dataclasses import dataclass


@dataclass
class Car():

    name: str
    color: str
    year: int

    def drive(self):
        print(f"The car {self.name} drives smoother")

    def year_of_making(self):
        print(f"The year of manufacturing is {self.year}")