"""
1.	Cree un diagrama de flujo que le pida 5 números al usuario y muestre el mayor. 
1.	Ejemplos: 
1.	4, 76, 43, 6, 8 → 76
2.	1, 2, 3, 6, 7 → 7
3.	2132, 4355, 1132, 2323, 1214 → 4355

"""

def largest_number():
    # We validate only numbers

    try:
        # We ask the user for the numbers
        first_number = int(input("Please enter the first number: "))
        second_number = int(input("Please enter the second number: "))
        third_number = int(input("Please enter the third number: "))
        fourth_number = int(input("Please enter the fourth number: "))
        fifth_number = int(input("Please enter the fifth number: "))

        # We store the numbers in a list

        stored_numbers = [first_number, second_number, third_number, fourth_number, fifth_number]

        # With max we get the largest number from the list
        largest = max(stored_numbers)


        # Show result        
        print(f"The entered numbers are: {first_number}, {second_number}, {third_number}, {fourth_number} and {fifth_number} and the largest among them is: {largest}")

    except ValueError:
        print("Error, you can only enter numeric values")

largest_number()

