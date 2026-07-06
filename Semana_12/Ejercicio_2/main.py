# This is the main file. It controls the shapes menu

from Sharpes import Circle, Rectangle, Square
from menu import menu_option


def main():

    # Main program loop
    while True:

        # Display the menu and get the user's choice
        option = menu_option()

        # Circle option
        if option == 1:

            try:

                # Request the circle radius
                radius = float(
                    input("Please enter the radius of the circle: ")
                )

                # Create a Circle object
                circle = Circle(radius)

                print("*****************************************************")

                # Display the circle area
                print(
                    f"The area of the circle is: "
                    f"{circle.calculate_area():.2f}"
                )

                # Display the circle perimeter
                print(
                    f"The perimeter of the circle is: "
                    f"{circle.calculate_perimeter():.2f}"
                )

                print("*****************************************************")

                # Pause before returning to the menu
                input("\nPress Enter to return to menu...")

            except ValueError as e:

                print(f"Error: {e}")

                input("\nPress Enter to return to menu...")

        # Square option
        elif option == 2:

            try:

                # Request the square side length
                side = float(
                    input("Please enter the side of the square: ")
                )

                # Create a Square object
                square = Square(side)

                print("*****************************************************")

                # Display the square area
                print(
                    f"The area of the square is: "
                    f"{square.calculate_area():.2f}"
                )

                # Display the square perimeter
                print(
                    f"The perimeter of the square is: "
                    f"{square.calculate_perimeter():.2f}"
                )

                print("*****************************************************")

            except ValueError as e:

                print(f"Error: {e}")

            # Pause before returning to the menu
            input("\nPress Enter to return to menu...")

        # Rectangle option
        elif option == 3:

            try:

                # Request the rectangle dimensions
                width = float(
                    input("Please enter the width of the rectangle: ")
                )

                height = float(
                    input("Please enter the height of the rectangle: ")
                )

                # Create a Rectangle object
                rectangle = Rectangle(width, height)

                print("*****************************************************")

                # Display the rectangle area
                print(
                    f"The area of the rectangle is: "
                    f"{rectangle.calculate_area():.2f}"
                )

                # Display the rectangle perimeter
                print(
                    f"The perimeter of the rectangle is: "
                    f"{rectangle.calculate_perimeter():.2f}"
                )

                print("*****************************************************")

            except ValueError as e:

                print(f"Error: {e}")

            # Pause before returning to the menu
            input("\nPress Enter to return to menu...")

        # Exit option
        elif option == 4:

            print("Goodbye!")
            break


# Execute the program
if __name__ == "__main__":

    main()