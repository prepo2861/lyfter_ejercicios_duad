"""
Cree un diagrama de flujo que le pida 100 números al usuario y muestre la suma de todos.
"""

def sum_numbers():
    # We validate so that only numbers are entered
    try:
        numbers_list = []  # We create the list to store the entered values

        for i in range(100):  # We create the loop that will request all the numbers
            number = int(input(f"Enter number {i+1}: "))
            numbers_list.append(number)  # The numbers are stored in the list

        result = sum(numbers_list)  # We sum all the values in the list

        print(f"The result of the sum of the entered numbers is: {result}")  # result

    except ValueError:
        print("Error, you can only enter numbers")

sum_numbers()
