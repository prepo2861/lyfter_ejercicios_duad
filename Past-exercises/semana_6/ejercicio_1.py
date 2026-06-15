"""
Cree dos funciones que impriman dos cosas distintas, y haga que la primera llame la segunda.
"""

def generate_number():  # Generate the first function to get the first number
    num_1 = int(input("Enter a number: "))  # Ask the user for the value
    return num_1  # Return the value to use it outside the function

def generate_result():  # Generate the second function to call the second number and get the result
    num_1 = generate_number()  # Bring the first value from the previous function
    num_2 = int(input("Enter a second number: "))  # Request the second value

    result = num_1 + num_2  # Perform the addition
    print(f"The result of the sum between {num_1} + {num_2} = {result}")  # Show the result

generate_result()  # Call the function that shows the entire exercise

    



