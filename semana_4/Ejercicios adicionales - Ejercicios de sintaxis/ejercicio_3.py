"""
3.	Cree un algoritmo que le pida un numero al usuario, y realice una suma de cada número del 1 hasta ese número ingresado. 
Luego muestre el resultado de la suma. 
1.	5 → 15 (1 + 2 + 3 + 4 + 5)
2.	3 → 6 (1 + 2 + 3)
3.	12 → 78 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10 + 11 + 12)

"""

def sum_numbers():
    # We validate so that the user only enters numbers and not letters or blank spaces

    try:
        number = int(input("Enter the number you want to display on screen: "))
        total = 0
        for i in range(1, number + 1):  # We use for in range to set the start, end, and step to reach the desired result.
            total = total + i  # total will give me the result of the sum of each number up to the entered number

            # Result

        print(f"The sum up to {number} is {total}")
    
    except ValueError:
        print("Error, you can only enter numeric values")

sum_numbers()
