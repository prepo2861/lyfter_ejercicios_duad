"""
Cree una función que reciba una lista de palabras y un número n, y retorne una nueva lista con solo las palabras que tengan más de n letras

"""
def create_list_of_words(count = 0):

    try:
        words_list = []  # Create an empty list to store the words entered by the user
        new_list = []  # Create another empty list to store the filtered words by length

        count_input = input("How many words are you going to enter in the list?: ")  # Ask for the number of words
        if not count_input.isdigit():  # Check that the input is a valid integer
            raise ValueError("You must enter only integer numbers")

        count_num = int(count_input)  # Convert input to integer after validation

        if count_num <= 0:
            raise ValueError("You can only enter positive numbers")  # Raise an error if condition is not met
            
        for i in range(count_num):  # Repeat the loop as many times as specified
                
            word = input(f"Enter word number {i+1}: ")  # Ask the user for each word

            if (
                not word.strip()  # empty
                or any(char.isdigit() for char in word)  # contains numbers
                or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in word)  # contains invalid symbols
            ):
                raise ValueError("You can only enter words (without numbers or symbols)")  # Error message

            words_list.append(word)  # Add the word to the list

        print(f"The original list is: {words_list}")  # Show the original list of words

        count_input = input("Enter the number of letters to filter the words: ")  # Ask for the number of letters to filter

        if not count_input.isdigit():  # Check again that the input is a valid integer
            raise ValueError("You must enter only integer numbers")

        count = int(count_input)

        if count <= 0:
            raise ValueError("You must enter a value greater than 0")  # Error message if the input is not valid

        for count_word in words_list:  # Loop through the list of words
             
            if len(count_word) == count:  # Compare each word’s length with the specified number
                new_list.append(count_word)  # Add to the new list if it matches

        print(f"The new list with words of {count} letters is: {new_list}")  # Show the filtered list
             

    except ValueError as error:
        print("Error:", error)  # Display the custom error message
        return  # Stop the program execution when an error occurs
        

create_list_of_words()


    