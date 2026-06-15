'''2. Use la función `print()` para mostrar resultados de operaciones matemáticas básicas.
    1. Por ejemplo:
        1. 1 + 1 → 2
        2. 90 + 430 → 520
        3. 4 * 5 → 20'''

import sys # Import sys to make interaction with the end user easier

def Basic_Operations(): # Define the function to work on basic operations
    try: # Use try to create validation handling

        try: # Create a try for each value to verify that the input is a numeric value
            num1 = int(input("Enter a number: "))
        except ValueError:
            raise ValueError("You must enter a valid number") # Error message if the user does not enter a correct value or leaves the input blank
        
        try:
            num2 = int(input("Enter a number: "))
        except ValueError:
            raise ValueError("You must enter a valid number")
        
        # Basic operations with the entered numbers

        sum = num1 + num2
        res = num1 - num2
        mul = num1 * num2
        div = num1 / num2
            
        # Display the result of the operations with the entered numbers on the console

        print("*****************************************************************************************")  
        print(f"The numbers entered were: {num1} and {num2} \nThe sum result is: {sum} \nThe subtraction result is: {res} \nThe multiplication result is: {mul} \nThe division result is: {div}")
        print("*****************************************************************************************")  


    except ValueError as e: # Except to capture errors and display the message on the console
        print("Error!", e)
        sys.exit(1)


Basic_Operations() # Call the function to work on it
