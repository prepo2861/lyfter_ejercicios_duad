"""
⭐ Ejercicios Extra

1. Cree un programa que:
- Pida al usuario su **nombre**
    - Si el nombre es numérico (`isdigit()`), **haga `raise ValueError("El nombre no puede ser un número")`**
"""


def only_strings_name():
    try:
        # Ask for the name from the user
        name = input("Enter your name:  ")

        # Name validations
        if (
            not name.strip()                         # Avoids empty entries or only spaces
            or any(char.isdigit() for char in name)  # The name must not contain numbers
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in name)  # Symbols are not allowed
            or name[0].isspace()                     # Spaces at the beginning are not allowed
        ):
            # Error message if any validation fails
            raise ValueError("You can only enter words (without numbers or symbols)")
        
        # If everything is correct, the valid name is returned
        return name

    except ValueError as e:
        print("Error!", e)
        return None
    

def only_strings_age(name):
    try:
        # Request the age from the user
        age = input("Enter your age:   ")

        # Age validations
        if (
            not age.isdigit()                        # Must be only numbers
            or not age.strip()                       # Avoids spaces and empty strings
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in age)  # Symbols are not allowed
            or age[0].isspace()                      # Spaces at the beginning are not allowed
        ):
            raise ValueError("You can only enter numeric values without blank spaces")
    
        # Convert age to integer
        age_int = int(age)

        # Validate that age is greater than 0
        if age_int <= 0:
            raise ValueError("Age must be greater than 0")
        
        # Show the result
        print(f"Hello! {name}, your age is: {age_int} years")

    except ValueError as e:
        print("Error!", e)
        return None
    

# Program execution
my_name = only_strings_name()
if my_name is not None:         # If the name was valid
    my_int = only_strings_age(my_name)   # Age is requested

