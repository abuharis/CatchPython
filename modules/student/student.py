from dataclasses import dataclass

@dataclass()
class Student():

    name: str
    age: int

    def enroll(self):
        print("I am enrolled into a course")

    def write_exam(self):
        print("I have written an exam")