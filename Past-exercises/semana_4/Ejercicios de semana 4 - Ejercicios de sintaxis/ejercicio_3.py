"""
3. Cree un programa con un numero secreto del 1 al 10. El programa no debe cerrarse hasta que el usuario adivine el numero.
    1. Debe investigar cómo generar un número aleatorio distinto cada vez que se ejecute.
"""

import random  # We import the random module to generate random numbers.
import sys

def guess_number():
    winner = random.randint(1, 10) # We will generate random numbers between 1 to 10

    while True: 
        try: #We will need the try except to force the user enter only numbers.
            number = int(input("Please enter a number between 1 and 10: "))

            if number < 1 or number > 10:
                print("You must enter a number between 1 and 10")
                continue  # Asks for the number again

        except ValueError:
            print("⚠️ You must enter a valid number (only digits)")
            continue  # Asks for the number again

        # Comparison with the winning number
        if number == winner:
            print("************************************")
            print("🎉🎉 Congratulations, you guessed it! 🎉🎉")
            print("************************************")
            break
        elif number < winner:
            print("The secret number is higher. Try again.")
        else:
            print("The secret number is lower. Try again.")

# Run
guess_number()

