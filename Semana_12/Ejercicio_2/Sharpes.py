from abc import ABC, abstractmethod
import math


# Abstract base class for all shapes
class Shape(ABC):

    # Abstract method to calculate the perimeter
    @abstractmethod
    def calculate_perimeter(self):
        pass

    # Abstract method to calculate the area
    @abstractmethod
    def calculate_area(self):
        pass


# Class that represents a circle
class Circle(Shape):

    # Initialize the circle radius
    def __init__(self, radius):

        # Validate that the radius is positive
        if radius <= 0:
            raise ValueError(
                "Radius must be a positive number."
            )

        # Store the radius value
        self.radius = radius

    # Calculate and return the circle perimeter
    def calculate_perimeter(self):

        return 2 * math.pi * self.radius

    # Calculate and return the circle area
    def calculate_area(self):

        return math.pi * self.radius ** 2


# Class that represents a square
class Square(Shape):

    # Initialize the square side length
    def __init__(self, side):

        # Validate that the side length is positive
        if side <= 0:
            raise ValueError(
                "Side must be a positive number."
            )

        # Store the side length
        self.side = side

    # Calculate and return the square perimeter
    def calculate_perimeter(self):

        return 4 * self.side

    # Calculate and return the square area
    def calculate_area(self):

        return self.side ** 2


# Class that represents a rectangle
class Rectangle(Shape):

    # Initialize the rectangle dimensions
    def __init__(self, width, height):

        # Validate that width and height are positive
        if width <= 0 or height <= 0:

            raise ValueError(
                "Width and height must be positive numbers."
            )

        # Store the rectangle dimensions
        self.width = width
        self.height = height

    # Calculate and return the rectangle perimeter
    def calculate_perimeter(self):

        return 2 * (self.width + self.height)

    # Calculate and return the rectangle area
    def calculate_area(self):

        return self.width * self.height