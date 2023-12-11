class Student:

    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    """New line after the error"""
    def __add__(self, other):
        m1 = self.m1 + other.m1
        m2 = self.m2 + other.m2
        s3 = Student(m1, m2)
        return s3

    """The add, gt, sub etc takes two object as parameters self and other.
    This is used to add objects within python, nothing to do with data types
    """


    def __gt__(self, other):    #self is the first
        r1 = self.m1 + other.m2     #2nd_obj.first_param + 2nd_obj.2nd_param
        r2 = self.m1 + other.m2
        if r1 > r2:
            return True
        else:
            return False


    def __eq__(self, other):
        value_1 = self.m1 + other.m1
        value_2 = self.m1 + other.m2
        if value_1 == value_2:
            return True
        else:
            return False


s1 = Student(50, 60)  #--> Student.__add__(1st_object, 2nd_object)
s2 = Student(40,20)   #--> Student.__add__(self, other) in this case s1 is the first object and s2 is the second object

"""If try to execute the code with + operator, it will throw an error that it is not supported.
In that case, we explicitly have to define an __add__ method to define it.
"""

s3 = s1 + s2
print(s3.m2)
print(s3.m1)

if s1 > s2:
    print("S1 wins")
else:
    print("s2 wins")

if s1 == s2:
    print("both are equal")
else:
    print("both objects are not equal")
