"""
7. Cree una función que acepte una lista de números y retorne una lista con los números primos de la misma.
    1. [1, 4, 6, 7, 13, 9, 67] → [7, 13, 67]

"""


def add_numbers():
    try:
        numbers_list = []  # Here the numbers entered by the user will be stored.

        count_num = int(input("How many numbers will you enter in the list?: "))  # Asks how many numbers will be entered

        if count_num <= 0:
            raise ValueError("You can only enter positive numbers")  # Raises an error if the condition is not met
        
        for i in range(count_num):  # Repeats the cycle the indicated number of times
            num = int(input(f"Enter number {i+1}: "))
            numbers_list.append(num)  # Saves the number in the list

        return numbers_list  # Returns the list with all the numbers

    except ValueError as e:  # Catches ValueError errors in case the user enters letters
        print("Error:", e)
        return []  # Returns an empty list in case of error


def is_prime(number):
    if number <= 1:  # Checks if the number is less than or equal to 1
        return False
    for i in range(2, int(number ** 0.5) + 1):  # Iterates through possible divisors
        if number % i == 0:  # If the remainder is 0, it means it has a divisor → it is not prime.
            return False  # Stops the loop and marks the number as not prime.
    return True  # If no divisors were found, it is prime


def show_prime_numbers(my_list):
    primes = []  # Here only the prime numbers will be stored.
    for number in my_list:  # Iterates through each number in the list
        if is_prime(number):  # Calls the previous function
            primes.append(number)  # Adds them to the new primes list.

    if primes:
        print(f"The prime numbers in the list are: {primes}")  # Shows the prime numbers found
    else:
        print("There are no prime numbers in the list.")  # Informs that none were found.



numbers = add_numbers()         # Creates the list
show_prime_numbers(numbers)     # Passes the list to the other function
