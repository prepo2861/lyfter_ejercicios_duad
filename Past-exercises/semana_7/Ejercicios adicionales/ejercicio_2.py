"""
1. Cree una función `convertir_a_entero(lista)` que:
- Reciba una lista de strings
- Intente convertir cada elemento a entero usando `int()`
- Use `try-except` para atrapar los errores `ValueError`
- Si algún elemento no puede convertirse, mostrar `"No se pudo convertir el elemento: <valor>"` y continuar con los demás

"""
def convert_to_integer(my_list=[]):
    
    try:
        # Asks the user for the number of elements they want to enter
        cont = input("How many elements do you want to enter in the list?: ")

        # Validations to ensure the entered quantity is valid
        if (
            not cont.isdigit()                        # Must contain only numbers
            or not cont.strip()                       # Avoids empty strings or only spaces
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in cont)  # Does not allow symbols
            or cont[0].isspace()                      # Does not allow spaces at the beginning
        ):
            raise ValueError("You can only enter numeric values without blank spaces")
        
        # Convert the received quantity to integer
        cont_int = int(cont)

        # Loop to request each element of the list
        for i in range(cont_int):
            my_elements = input(f"Enter value number {i+1} for the list:  ")

            # Save the original input to print it in the messages
            original_value = my_elements  

            try:
                # Try to convert to number (float if it contains a decimal point)
                if "." in my_elements:
                    converted = float(my_elements)   # Converts decimals
                else:
                    converted = int(my_elements)     # Converts integers

                # Successful conversion message
                print(f'"{original_value}" converted to {converted}')
                my_elements = converted  # Replace the original value with the converted value

            except ValueError:
                # If an error occurs in the conversion, show message
                print(f"Could not convert the element: {original_value}")

            # Add the element (converted or not) to the list
            my_list.append(my_elements)

        # Show the final list after processing
        print("\nFinal result:")
        print(my_list)
      
    except ValueError as e:
        # Catches and shows initial validation errors
        print("Error!", e)


# Call to the main function
convert_to_integer()


