"""
1. Cree un algoritmo que muestre cuántos años tendrá usted dentro de 10 años. El algoritmo debe usar `print()` y una operación de suma
- Ejemplo:
    - Salida:
        
        ```python
        "Dentro de 10 años yo tendré 37 años" 
        ```
"""

import sys

def Age(): # Define the function we are going to work on

    try:

        name = input("Enter your name: ") # Request the user's name


        # Validate that the name does not contain numbers or special characters
        if not name.strip() or any(char.isdigit() for char in name) or any(char in name for char in ['+', '-', '*', '/', '=', '!', '@', '#', '$', '%', '^', '&', '(', ')', '[', ']', ';', ':', '"', '{', '}']):
            raise ValueError("You cannot leave empty spaces or enter special characters.")
        
        # Request and validate the age
        try:
            age = int(input("Enter your age: "))
            if age < 0:
                raise ValueError("You cannot enter a number less than 0.")
        except ValueError:
            raise ValueError("Please enter a valid number for the age.")
        
        # Calculate the new age

        New_Age = age + 10

        # Display the result
        print("*****************************************************************************************")
        print(f"Hello, my name is: {name} \nMy age is: {age} \nIn 10 years I will be: {New_Age}")
        print("*****************************************************************************************")



    except ValueError as e: # Except to capture errors and display the message on the console
        print("Error!", e)



Age() # Call the function to display the results on the console