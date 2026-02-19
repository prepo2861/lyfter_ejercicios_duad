"""
1. Cree una función que reciba un texto y un carácter, y retorne cuántas veces aparece ese carácter en el texto

"""

def traverse_list(count=0):  # Create the function with a counter parameter that will show the number of letters in a text
    try:

        my_string = input(f"Enter a text:  ")  # Ask for the text

        if (
            not my_string.strip()  # empty
            or any(char.isdigit() for char in my_string)  # contains numbers
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in my_string)  # symbols not allowed
        ):
            raise ValueError("You can only enter words (without numbers or symbols)")  # Error message
    
        my_letter = input(f"Enter a letter to search in the text:  ")  # Ask for the letter

        if (
            not my_letter.strip()  # empty
            or any(char.isdigit() for char in my_letter)  # contains numbers
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in my_letter)  # symbols not allowed
        ):
            raise ValueError("You can only enter words (without numbers or symbols)")  # Error message
        
        for i in range(len(my_string)):  # Traverse the text

            if my_string[i] == my_letter:  # Compare if we find the requested letter
                count += 1  # The counter will add up each time it finds the letter

                       
        if count > 0:  # If there are results, show the message with the number of letters in the text
            print(f"The letter {my_letter} was found in the word {my_string}, {count} times")
        else:  # Show that the letter was not found in the word if not found
            print(f"That letter was not found in the word {my_string}")

    except ValueError as error:
        print("Error", error)

traverse_list()
