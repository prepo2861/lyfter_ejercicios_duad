"""
1. Cree una función `sumar_valores(lista)` que:
- Reciba una lista de elementos (strings, enteros, flotantes mezclados)
- Intente convertir cada elemento a tipo `float`
- Si puede, sume el valor y muestre: `"<valor> sumado correctamente"`
- Si no puede, muestre: `"Elemento inválido: <valor>"`
- Al final, imprima la suma total
"""

def sum_values(my_list=[], my_list_num=[]):
    try:

        # Asks the user how many elements they will enter
        cont = input("How many elements do you want to enter in the list?: ")

        # Validations to ensure the entered quantity is valid
        if (
            not cont.isdigit()                         # Must contain only numbers
            or not cont.strip()                        # Avoids empty strings or only spaces
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in cont)  # Does not allow symbols
            or cont[0].isspace()                       # Does not allow spaces at the beginning
        ):
            raise ValueError("You can only enter numeric values without blank spaces")
        
        # Convert the entered quantity to integer
        cont_int = int(cont)

        # Loop to request each element that the user will introduce
        for i in range(cont_int):

            # Ask for value from the user
            my_elements = input(f"Enter value number {i+1} for the list:  ")

            # Save the original input in case it cannot be converted
            original_value = my_elements  

            try:
                # Try to convert to a number
                if "." in my_elements:
                    converted = float(my_elements)     # If it contains a point, convert to float
                else:
                    converted = int(my_elements)       # Otherwise, convert to integer

                # Message indicating that the conversion was successful
                print(f'{converted} added correctly')

                # Replace original value with converted value
                my_elements = converted  

                # Save only the converted numbers in a separate list
                my_list_num.append(converted)

            except ValueError:
                # If an error occurs when converting, notify the user
                print(f"Invalid element: {original_value}")

            # Always add the element (converted or not) to the original list
            my_list.append(my_elements)

            # Sum all the converted numeric values
            result = sum(my_list_num)
               
            # Show partial results in each iteration
        print("\nOriginal list:")
        print(my_list)

        print("\nSum result: ")
        print(f"{my_list_num} = {round(result,2)}")

    except ValueError as e:
        # General error handling
        print("Error!", e)


# Function call
sum_values()

