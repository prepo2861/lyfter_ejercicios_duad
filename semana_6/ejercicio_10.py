"""
Cree una función que reciba un string y retorne cuántas vocales contiene

"""

def count_vowels(count = 0, vowels = "AEIOUaeiou"):  # Create the function with parameters: one to count vowels and another that contains the vowels
    try:
        my_string = input("Enter a word: ")  # Ask the user to input a word

        if (
            not my_string.strip()  # empty
            or any(char.isdigit() for char in my_string)  # contains numbers
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in my_string)  # symbols not allowed
        ):
            raise ValueError("You must enter words only!")  # Error message if invalid input is detected
        
        for letter in my_string:  # Loop through each character in the word
            if letter in vowels:  # Check if the character is a vowel
                count += 1  # Add 1 to the counter for each vowel found

        print(f"The word '{my_string}' contains {count} vowels")  # Display the result

    except ValueError as error:
        print("Error:", error)  # Show the error message if a ValueError occurs

count_vowels()
