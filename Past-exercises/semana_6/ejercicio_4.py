"""
4. Cree una función que le de la vuelta a un string y lo retorne.
    1. Esto ya lo hicimos en iterables.
    2. “Hola mundo” → “odnum aloH”

"""

def turn_string(my_string="Hola mundo"):  # Create the function with the requested parameter

    print(my_string)  # Show the parameter in console
     
    my_reversed_string = my_string[::-1]  # Reverses the text

    print(my_reversed_string)  # Show the already modified text


turn_string()
