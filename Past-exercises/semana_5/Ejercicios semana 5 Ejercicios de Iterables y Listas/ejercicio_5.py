"""
5. Cree un programa que le pida al usuario 10 números, y al final le muestre todos los números que ingresó, seguido del numero ingresado más alto.
    1. Ejemplos:
    2. 86, 54, 23, 54, 67, 21, 2, 65, 10, 32 → [86, 54, 23, 54, 67, 21, 2, 65, 10, 32]. El más alto fue 86.

"""

def exercise_5():

    my_list = []  # we create an empty list

    for i in range(10):  # We make a for loop to consider that we only need 10 numbers
        number = int(input(f"Enter the value number {i+1}: "))  # We ask the user for the numbers

        my_list.append(number)  # we add the numbers to the empty list
        greater = max(my_list)  # We find the largest number in the list

    print(f"The entered list is: {my_list} and the largest number is {greater}")  # We show the result

exercise_5()
