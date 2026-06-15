"""
4. Cree un programa que le pida tres números al usuario y muestre el mayor.
"""

import sys

def largest_number():
    try:  # We use try to validate that the user can only enter numeric values
        number_1 = int(input("Enter the first number: "))
        number_2 = int(input("Enter the second number: "))
        number_3 = int(input("Enter the third number: "))

        # Assume the largest is the first one
        largest = number_1

        # We use an if to compare the numbers so we can determine which is the largest among the three

        if number_2 > largest:
            largest = number_2
        if number_3 > largest:
            largest = number_3

        print(f"The largest number among {number_1}, {number_2} and {number_3} is: {largest}")

    except ValueError:
        print("Error: You must enter only numbers.")  # Error message if the user does not enter numeric values

largest_number()

