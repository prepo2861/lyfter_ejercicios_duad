"""
5. Cree una función que imprima el numero de mayúsculas y el numero de minúsculas en un string.
    1. “I love Nación Sushi” → “There’s 3 upper cases and 13 lower cases”
"""

def num_upper_and_lower(count_lower= 0, count_upper= 0, my_string= "I love Nacion Sushi"):  # Create the function with parameters
  

    for letter in my_string:  # Traverse the string

        if letter.islower():  # Search for lowercase letters and add them to the counter
            count_lower += 1

        elif letter.isupper():  # In case of finding uppercase letters, do the same
            count_upper += 1

    print(f"The word {my_string} has: {count_upper} uppercase letters and {count_lower} lowercase letters")  # Show the final result

num_upper_and_lower()

