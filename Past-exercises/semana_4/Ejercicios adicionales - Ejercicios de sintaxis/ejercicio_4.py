"""
1.	Cree un algoritmo que le pida 2 números al usuario, los guarde en dos variables distintas 
(primero y segundo) y los ordene de menor a mayor en dichas variables
"""

def sort_numbers():
    # We validate so that the user only enters numeric values
    try:
        # We define these variables to store the numbers from largest to smallest
        largest_number = 0
        smallest_number = 0

        # We request the numbers from the user

        number_1 = int(input("Please enter the first number to compare: "))
        number_2 = int(input("Please enter the second number to compare: "))

        # We compare the two entered numbers

        if number_1 > number_2:
            largest_number = number_1
            smallest_number = number_2
            print(f"The largest entered number is {largest_number} and then comes {smallest_number}")
        elif number_2 > number_1:
            largest_number = number_2
            smallest_number = number_1
            print(f"The largest entered number is {largest_number} and then comes {smallest_number}")
        else:
            print("The two entered numbers are equal")
        
            

    except ValueError:
        print("Error, you can only enter numeric values")

sort_numbers()
