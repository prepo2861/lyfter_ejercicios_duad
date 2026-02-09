"""
4.	Cree un diagrama de flujo que le pida 100 números al usuario y muestre el mayor de todos. 
"""

def largest_number():
    # We validate so that only numbers are entered
    try:
        numbers_list = []  # We create the list to store the entered values

        for i in range(100):  # We create the loop that will request all the numbers
            number = int(input(f"Enter number {i+1}: "))
            numbers_list.append(number)  # The numbers are stored in the list

            result = max(numbers_list)  # We get the largest number from all the entered numbers

        print(f"The largest number among the entered numbers is: {result}")  # result

    except ValueError:
        print("Error, you can only enter numbers")

largest_number()
