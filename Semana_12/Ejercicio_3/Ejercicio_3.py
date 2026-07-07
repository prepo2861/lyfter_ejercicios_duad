"""
Research the uses of multiple inheritance and create an example.
"""

"""
Answer:

Multiple inheritance allows a class to inherit attributes and methods
from more than one parent class.

Some common uses are:

1. Combining behaviors:
   An object can have characteristics from multiple classes.

2. Code reuse:
   It avoids duplicating methods that already exist in other classes.

3. Modeling complex entities:
   When an object belongs to multiple categories at the same time.
"""


# Class for studying
class Student:

    # Method that represents studying
    def study(self):

        print("Studying for an exam...")


# Class for working
class Employee:

    # Method that represents working
    def work(self):

        print("Working on a project...")


# WorkingStudent inherits from both Student and Employee
class WorkingStudent(Student, Employee):

    pass


# Create an instance of WorkingStudent
person = WorkingStudent()

# Call methods inherited from both parent classes
person.study()
person.work()