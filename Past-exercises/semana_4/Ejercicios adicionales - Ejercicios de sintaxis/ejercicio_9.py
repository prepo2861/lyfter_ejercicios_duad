"""
2.	Cree un diagrama de flujo que le pida un numero al usuario y muestre “Fizz” si es divisible entre 3, 
    “Buzz” si es divisible entre 5, y “FizzBuzz” si es divisible entre ambos. 
1.	Ejemplos: 
1.	33 → Fizz
2.	25 → Buzz
3.	30 → FizzBuzz

"""

def fizzbuzz():
    # We perform the corresponding validations so that only positive numbers are generated.
    try:
        number = int(input("Enter a number: "))
        if number < 0:
            raise ValueError
        
        # We use the conditional to confirm if the entered number meets the requirements and display the result
        
        if number % 5 == 0 and number % 3 == 0:
            print("FizzBuzz")
        elif number % 5 == 0:
            print("Buzz")
        elif number % 3 == 0:
            print("Fizz")
        else:
            print("The entered number cannot be divided by 3 and 5")

    except ValueError:
        print("Error, you can only enter positive numbers")

fizzbuzz()

