"""
Cree una clase Rectangle que:
Tenga atributos width y height
Tenga un método get_area() que retorne el área
Tenga un método get_perimeter() que retorne el perímetro
Valide que ningún valor sea negativo. Si lo es, lance una excepción con un mensaje adecuado

"""

"""
Create a Rectangle class that:
- Has width and height attributes
- Has a get_area() method that returns the area
- Has a get_perimeter() method that returns the perimeter
- Validates that no value is negative
- Raises an exception with an appropriate message if a value is negative
"""


class Rectangle:

    # Constructor used to initialize a Rectangle object
    def __init__(self, width, height):

        # Validate that width and height are not negative
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")

        # Store the rectangle dimensions
        self.width = width
        self.height = height

    # Calculate and return the rectangle area
    def get_area(self):
        return self.width * self.height

    # Calculate and return the rectangle perimeter
    def get_perimeter(self):
        return 2 * (self.width + self.height)


# Keep asking for input until valid values are entered
while True:

    try:

        # Ask the user for the rectangle width
        width = float(input("Please enter the width: "))

        # Ask the user for the rectangle height
        height = float(input("Please enter the height: "))

        # Create a Rectangle object
        rect = Rectangle(width, height)

        # Exit the loop if the rectangle was created successfully
        break

    except ValueError as e:

        # Display the error message and ask again
        print(f"Error: {e}")


# Display the rectangle area formatted to 2 decimal places
print(f"The area of the rectangle is: {rect.get_area():.2f}")

# Display the rectangle perimeter formatted to 2 decimal places
print(f"The perimeter of the rectangle is: {rect.get_perimeter():.2f}")

    
        