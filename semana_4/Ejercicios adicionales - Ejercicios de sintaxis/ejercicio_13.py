"""
4. **Tabla de multiplicar personalizada**
    - Pida al usuario un número del 1 al 10
    - Muestre su tabla de multiplicar del 1 al 12
"""

def multiplication():
    # We create validations so that only positive numbers are entered
    try:
        number = int(input("Enter a number from 1 to 10 to display its multiplication table: "))
        
        if number < 1 or number > 10:  # We validate that only numbers from 1 to 10 can be entered
            raise ValueError
        
        for i in range(1, 13):  # We use the for loop to form the multiplication table
            result = number * i  # The multiplication of the values
            
            print(f"{number} x {i} = {result}")  # result

    except ValueError:
        print("Error, you can only enter positive numbers from 1 to 10")

multiplication()
