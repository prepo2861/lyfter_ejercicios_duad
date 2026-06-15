"""
Cree un programa que le pida al usuario ingresar 5 palabras. Luego muestre una nueva lista con solo aquellas palabras que tengan más de 4 letras

"""

def exercise_10():
    try:
        my_list = []  # We create the empty list

        query = int(input("How many words do you want to enter in the list?: "))

        if query <= 0:
            raise ValueError("You can only enter positive values")

        for i in range(query):  # We ask for the words one by one
            word = input(f"Enter the word number {i + 1}: ")

            # Input validation: not empty, without digits or special symbols
            if (
                not word.strip()  # empty
                or any(char.isdigit() for char in word)  # contains numbers
                or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in word)  # symbols not allowed
            ):
                raise ValueError("You can only enter words (without numbers or symbols)")

            my_list.append(word)

        # Create a new list with words longer than 4 letters
        new_list = [p for p in my_list if len(p) > 4]

        print(f"\nThe entered list is: {my_list}")
        print(f"The words with more than 4 letters are: {new_list}")

    except ValueError as e:
        print("Error:", e)


exercise_10()
