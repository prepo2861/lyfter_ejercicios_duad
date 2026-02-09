"""
2. Experimente con el concepto de scope:
    1. Intente accesar a una variable definida dentro de una función desde afuera.
    2.  Intente accesar a una variable global desde una función y cambiar su valor.
"""

import random  # Import the random library to generate random numbers

global_number = 5  # Define a global integer


def show_even_numbers():  # Function that attempts to modify a global variable

    global global_number  # Needed to modify the global variable inside the function

    if global_number % 2 != 0:  # If the global number is not even
        global_number = 6       # Change its value to an even number

    print(f"The new even number is: {global_number}")

    # NOTE:
    # Modifying global variables inside a function is not recommended.
    # This can create unexpected behavior because the value can change
    # in different parts of the program.
    # Global variables should only be used when absolutely necessary.


def show_any_number():
    numbers_of_function = random.randint(0, 99)
    print(f"The winning number is: {numbers_of_function}")


# Call the function
show_any_number()

# This line will cause a NameError
# because the variable numbers_of_function only exists inside the function.
print(f"Showing the winning number again: {numbers_of_function}")

show_even_numbers()


        