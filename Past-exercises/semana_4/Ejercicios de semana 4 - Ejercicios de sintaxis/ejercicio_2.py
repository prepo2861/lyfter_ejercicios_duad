"""
2. Cree un programa que le pida al usuario su nombre, apellido, y edad, y 
muestre si es un bebé, niño, preadolescente, adolescente, adulto joven, adulto, o adulto mayor.
"""

import sys

def define_user():
    try:
        # Let's ask the user for their first name and last name.
        first_name = input("Enter your first name: ")
        last_name = input("Enter your last name: ")

        # We will validate so that only text can be entered in first name and last name
        forbidden_characters = ['+', '-', '*', '/', '=', '!', '@', '#', '$', '%', '^', '&', '(', ')', ',', '[', ']', ';', ':', '"', '{', '}', '  ']

        # Remove spaces at the beginning and end of first name
        first_name = first_name.strip()

        # Check if it is empty
        if not first_name:
            raise ValueError("You cannot leave the first name blank")
        
        # Check if it contains numbers
        if any(char.isdigit() for char in first_name):
            raise ValueError("You cannot enter numbers in the first name")
        
        # Check if it contains forbidden characters
        if any(char in first_name for char in forbidden_characters):
            raise ValueError("You cannot enter special symbols in the first name")

        # Remove spaces at the beginning and end of last name
        last_name = last_name.strip()

        # Check if it is empty
        if not last_name:
            raise ValueError("You cannot leave the last name blank")
        
        # Check if it contains numbers
        if any(char.isdigit() for char in last_name):
            raise ValueError("You cannot enter numbers in the last name")
        
        # Check if it contains forbidden characters
        if any(char in last_name for char in forbidden_characters):
            raise ValueError("You cannot enter special symbols in the last name")
        
        # Define the age
        try:
            age = int(input("Enter your age:  "))

            # Validate that age is greater than 0 and that the user does not leave the space blank
            if age < 0:
                raise ValueError("You must enter an age greater than 0")
    
        except ValueError:
            raise ValueError("You must enter an age greater than 0 and not leave the age field blank")
        
        # Define if the user is a baby, child, preadolescent, adolescent, young adult, adult, or senior adult.

        if 0 <= age <= 2:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are a baby")
        elif 3 <= age <= 9:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are a child")
        elif 10 <= age <= 12:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are a preadolescent")
        elif 13 <= age <= 18:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are an adolescent")
        elif 19 <= age <= 35:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are a young adult")
        elif 36 <= age <= 59:
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are an adult")
        else:  # 60 or older
            print(f"Hello! {first_name} {last_name}, your age is {age} and you are a senior adult")

    except ValueError as e:
        print("Error", e)
        sys.exit(1)

        
define_user()