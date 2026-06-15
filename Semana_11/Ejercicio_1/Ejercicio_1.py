"""
Cree una clase Circle con:
- Un atributo radius (radio)
- Un método get_area que retorne su área
"""

# Imports the math module to use the value of pi
import math


# Class that represents a circle
class Circle:

    # Class constructor
    def __init__(self, radius):

        # Stores the radius of the circle
        self.radius = radius

    # Method to calculate the area of the circle
    def get_area(self):

        # Area formula:
        # π * radius²
        return math.pi * self.radius**2


# Asks the user for the circle radius
# and creates an instance of the Circle class
my_circle = Circle(float(input("Enter the circle radius: ")))


# Displays the circle area with 2 decimal places
print(f"The result is: {my_circle.get_area():.2f}")

