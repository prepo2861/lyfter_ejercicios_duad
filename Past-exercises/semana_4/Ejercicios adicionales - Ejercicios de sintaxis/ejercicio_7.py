"""
3.	Cree un diagrama de flujo que pida 3 números al usuario. 
    Si uno de esos números es 30, o si los 3 sumados dan 30, mostrar “Correcto”. Sino, mostrar “incorrecto”. 
1.	Ejemplos: 
1.	23, 30, 768 → Correcto (hay un 30)
2.	10, 15, 5 → Correcto (10 + 15 + 5 = 30)
3.	35, 56, 2 → Incorrecto (no hay ningún 30, y la suma de ellos tampoco da 30)

"""

def sum_numbers():
    # We define a list to store the numbers entered by the user

    numbers_list = []

    # We validate that only numbers are entered, not letters.
    try:
        for i in range(3):
            user_number = int(input(f"Please enter value # {i+1}: "))
            numbers_list.append(user_number)

        if 30 in numbers_list:  # We search for the number 30 in the list
            print("Correct, the number 30 is among the numbers you entered")
        elif sum(numbers_list) == 30:  # We sum the elements of the list to check if the result is 30
            print("The sum of the entered numbers is equal to 30")
        else:  # If there is no 30, indicate that there is no result
            print("Incorrect. There is no 30 and the sum of the numbers does not equal 30")
    except ValueError:
        print("Error, you must enter numeric values")

sum_numbers()
