"""
1. Cree una calculadora por linea de comando. Esta debe de tener un número actual, y un menú para decidir qué operación hacer con otro número:
1. Suma
2. Resta
3. Multiplicación
4. División
5. Borrar resultado
Al seleccionar una opción, el usuario debe ingresar el nuevo número a sumar, restar, multiplicar, o dividir por el actual. El resultado debe pasar a ser el nuevo numero actual.
Debe de mostrar mensajes de error si el usuario selecciona una opción invalida, o si ingresa un número invalido a la hora de hacer la operación.

"""

import sys


def request_first_number(current_value=0):

    try:
        # Display the current value to the user
        print("******************************")
        print(f"{current_value}")
        print("******************************")

        # Request the first number from the user
        last_input_value = input("Enter the first number:   ")

        # Validation of the entered data
        if (
            not last_input_value.strip()                       # Must not be empty or only spaces
            or last_input_value[0].isspace()                   # Cannot start with a space
            or any(char in '+-*/=!@#$%^&()[];:{}"<>?' for char in last_input_value)  # Symbols are not allowed
            or last_input_value.count('.') > 1                 # Only one decimal point allowed
            or not all(c.isdigit() or c == '.' for c in last_input_value)  # Only digits and period
        ):
            raise ValueError("You can only enter numbers. Letters, signs, or empty spaces are not allowed.")

        # Add the entered number to the current value
        current_value += float(last_input_value)

        # Return the updated value
        return current_value

    except ValueError as e:
        # Error message when the input is invalid
        print("Error:", e)
        return None



def show_menu(current_value, display_screen=None):
    try:
        # If no screen history is received, initialize as an empty list
        if display_screen is None:
            display_screen = []

        # Valid menu options
        menu = ["+", "-", "*", "/", "=", "C", "Exit"]
    
        # Request the user to select an operation
        selected_option = input(
            "Choose operation: \n"
            "+ , - , * , / , = , C (reset) or Exit: "
        )
        
        # Validate that the option is within the allowed menu
        if selected_option not in menu:
            raise ValueError("Invalid option, please try again!")
        
        # If the user resets (C), clear the screen and return immediately
        if selected_option == "C":
            display_screen.clear()
            return selected_option, display_screen
        
        # For mathematical operations, build the screen with history
        if selected_option in ["+", "-", "*", "/"]:
            
            # If the screen is empty, add the current value as the starting point
            if not display_screen:
                display_screen.append(str(current_value))

            # Avoid placing the same operator twice in a row
            if display_screen[-1] != selected_option:
                display_screen.append(selected_option)

            # Display the current expression on screen
            print("******************************")
            print(" ".join(display_screen))
            print("******************************")
            
            return selected_option, display_screen

        # For '=' or 'Exit', just return the option without modifying the screen
        return selected_option, display_screen

    except ValueError as e:
        # Handling invalid inputs
        print("Error:", e)
        return None, display_screen



    
def show_sum_result(current_value, operator, display_screen):

    while True:

        # ------------------------------------------------------
        # 1. Handle full reset when the operator is "C"
        # ------------------------------------------------------
        if operator == "C":
            print("Resetting...")

            # Clear the screen of previous operations
            display_screen.clear()

            # Request a new initial number
            current_value = request_first_number()
            if current_value is None:
                return

            # Request the first operator after resetting
            operator = input(
                "Choose operation: \n"
                "+ , - , * , / , = , C (reset) or Exit: "
            )

            # Validate the selected option
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using + by default.")
                operator = "+"

            continue

        # ------------------------------------------------------
        # 2. If the user presses "=", display the final result
        # ------------------------------------------------------
        if operator == "=":
            print(" ".join(display_screen))
            print(f"Final result: {current_value}")
            return

        # ------------------------------------------------------
        # 3. End program if "Exit" is selected
        # ------------------------------------------------------
        if operator == "Exit":
            print("End of program")
            sys.exit()

        # ------------------------------------------------------
        # 4. Request the next number to add
        # ------------------------------------------------------
        try:
            num_2 = input("Enter a number: ")

            # Complete input validation
            if (
                not num_2.strip()                         # no empty spaces
                or any(c in '+-*/=!@#$%^&()[];:{}",<>?' for c in num_2)  # no symbols
                or num_2[0].isspace()                    # no leading space
                or not all(c.isdigit() or c == '.' for c in num_2)  # only numbers or one period
            ):
                raise ValueError(
                    "You can only enter numbers. Letters, signs, or empty spaces are not allowed."
                )

            next_value = float(num_2)

        except ValueError as e:
            # Invalid input → show error and request operator
            print("Error:", e)

            operator = input(
                "Enter operator (+, -, *, /, =, C, Exit) or Enter to try again with addition: "
            )

            # Empty Enter means continue adding
            if operator == "":
                operator = "+"

            # If C is selected again here, reset
            if operator == "C":
                continue

            # Validation of the selected operator
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using + by default.")
                operator = "+"

            continue

        # ------------------------------------------------------
        # 5. Update the screen with operator and entered number
        # ------------------------------------------------------
        if not display_screen:
            # First operation after the initial value
            display_screen.append(str(current_value))

        # Add the operator if the last element is not an operator
        if display_screen[-1] not in ["+", "-", "*", "/"]:
            display_screen.append(operator)

        # Add the entered number to the expression
        display_screen.append(str(next_value))

        # ------------------------------------------------------
        # 6. Apply the addition operation
        # ------------------------------------------------------
        current_value += next_value

        # ------------------------------------------------------
        # 7. Display the updated operation status
        # ------------------------------------------------------
        print("******************************")
        print(" ".join(display_screen))
        print(f"Partial result: {current_value}")
        print("******************************")

        # ------------------------------------------------------
        # 8. Request next operator
        # ------------------------------------------------------
        operator = input(
            "Enter operator (+, -, *, /, =, C, Exit):  "
        )

        # Operator validation
        if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
            print("Invalid operator. Continuing with addition by default.")
            operator = "+"

        # Delegate based on the selected operation
        if operator == "-":
            return show_subtraction_result(current_value, "-", display_screen)

        if operator == "*":
            return show_multiplication_result(current_value, "*", display_screen)

        if operator == "/":
            return show_division_result(current_value, "/", display_screen)



def show_subtraction_result(current_value, operator, display_screen):

    while True:

        # ------------------------------------------------------
        # 1. Reset the process when the user selects "C"
        # ------------------------------------------------------
        if operator == "C":
            print("Resetting...")

            # Clear all history displayed on screen
            display_screen.clear()

            # Request a new initial value
            current_value = request_first_number()
            if current_value is None:
                return

            # Request a new starting operator
            operator = input(
                "Choose operation: \n"
                "+ , - , * , / , = , C (reset) or Exit: "
            )

            # Validate the selected option
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using - by default.")
                operator = "-"

            continue

        # ------------------------------------------------------
        # 2. If the operator is "=", finalize and display the result
        # ------------------------------------------------------
        if operator == "=":
            print(" ".join(display_screen))
            print(f"Final result: {current_value}")
            return

        # ------------------------------------------------------
        # 3. Close the entire program when "Exit" is chosen
        # ------------------------------------------------------
        if operator == "Exit":
            print("End of program")
            sys.exit()

        # ------------------------------------------------------
        # 4. Request the next number to subtract
        # ------------------------------------------------------
        try:
            num_2 = input("Enter a number: ")

            # Complete validation of the entered number
            if (
                not num_2.strip()                         # avoid empty spaces
                or any(c in '+-*/=!@#$%^&()[];:{}",<>?' for c in num_2)  # no symbols
                or num_2[0].isspace()                    # no leading space
                or not all(c.isdigit() or c == '.' for c in num_2)  # only digits or period
            ):
                raise ValueError(
                    "You can only enter numbers. Letters, signs, or empty spaces are not allowed."
                )

            next_value = float(num_2)

        except ValueError as e:
            # Invalid input → show error and request an operator
            print("Error:", e)

            operator = input(
                "Enter operator (+, -, *, /, =, C, Exit) or Enter to try again with subtraction: "
            )

            # Empty Enter → continue subtracting
            if operator == "":
                operator = "-"

            # If the user enters "C", reset everything
            if operator == "C":
                continue

            # Validate the entered operator
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using - by default.")
                operator = "-"

            continue

        # ------------------------------------------------------
        # 5. Record the executed operation on screen
        # ------------------------------------------------------
        if not display_screen:
            # First operation after the initial number
            display_screen.append(str(current_value))

        # Add the operator if the last element is not already an operator
        if display_screen[-1] not in ["+", "-", "*", "/"]:
            display_screen.append(operator)

        # Add the entered number to the expression
        display_screen.append(str(next_value))

        # ------------------------------------------------------
        # 6. Perform the subtraction
        # ------------------------------------------------------
        current_value -= next_value

        # ------------------------------------------------------
        # 7. Display the operation progress
        # ------------------------------------------------------
        print("******************************")
        print(" ".join(display_screen))
        print(f"Partial result: {current_value}")
        print("******************************")

        # ------------------------------------------------------
        # 8. Request the next operation
        # ------------------------------------------------------
        operator = input(
            "Enter operator (+, -, *, /, =, C, Exit):  "
        )

        # Operator validation
        if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
            print("Invalid operator. Continuing with subtraction by default.")
            operator = "-"

        # Delegation to the corresponding function based on operator
        if operator == "+":
            return show_sum_result(current_value, "+", display_screen)

        if operator == "*":
            return show_multiplication_result(current_value, "*", display_screen)

        if operator == "/":
            return show_division_result(current_value, "/", display_screen)

def show_multiplication_result(current_value, operator, display_screen):
   
    while True:

        # ------------------------------------------------------
        # 1. Reset everything when the user chooses "C"
        # ------------------------------------------------------
        if operator == "C":
            print("Resetting...")

            # Clear the history of operations displayed
            display_screen.clear()

            # Request the initial number again
            current_value = request_first_number()
            if current_value is None:
                return

            # Request the next operator
            operator = input(
                "Choose operation: \n"
                "+ , - , * , / , = , C (reset) or Exit: "
            )

            # Validate the chosen operator
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using * by default.")
                operator = "*"

            continue

        # ------------------------------------------------------
        # 2. Finalize operation with the "=" operator
        # ------------------------------------------------------
        if operator == "=":
            print(" ".join(display_screen))
            print(f"Final result: {current_value}")
            return

        # ------------------------------------------------------
        # 3. Completely close the application with "Exit"
        # ------------------------------------------------------
        if operator == "Exit":
            print("End of program")
            sys.exit()

        # ------------------------------------------------------
        # 4. Request number to multiply
        # ------------------------------------------------------
        try:
            num_2 = input("Enter a number: ")

            # Complete validation of the entered number
            if (
                not num_2.strip()                         # avoids empty strings
                or any(c in '+-*/=!@#$%^&()[];:{}",<>?' for c in num_2)  # avoids symbols
                or num_2[0].isspace()                    # no leading spaces
                or not all(c.isdigit() or c == '.' for c in num_2)  # only numbers and decimal point
            ):
                raise ValueError(
                    "You can only enter numbers. Letters, signs, or empty spaces are not allowed."
                )

            next_value = float(num_2)

        except ValueError as e:
            # Invalid input → request an alternative operator
            print("Error:", e)

            operator = input(
                "Enter operator (+, -, *, /, =, C, Exit) or Enter to try again with multiplication: "
            )

            if operator == "":
                operator = "*"

            # If the user decides to reset
            if operator == "C":
                continue

            # Ensure the operator is valid
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using * by default.")
                operator = "*"

            continue

        # ------------------------------------------------------
        # 5. Visually build the operation on screen
        # ------------------------------------------------------
        if not display_screen:
            display_screen.append(str(current_value))

        if display_screen[-1] not in ["+", "-", "*", "/"]:
            display_screen.append(operator)

        display_screen.append(str(next_value))

        # ------------------------------------------------------
        # 6. Perform the requested multiplication
        # ------------------------------------------------------
        current_value *= next_value

        # ------------------------------------------------------
        # 7. Display the operation progress
        # ------------------------------------------------------
        print("******************************")
        print(" ".join(display_screen))
        print(f"Partial result: {current_value}")
        print("******************************")

        # ------------------------------------------------------
        # 8. Consult the next operator to continue
        # ------------------------------------------------------
        operator = input(
            "Enter operator (+, -, *, /, =, C, Exit):  "
        )

        # Validate the chosen operator
        if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
            print("Invalid operator. Continuing with multiplication by default.")
            operator = "*"

        # Delegate based on the received operator
        if operator == "+":
            return show_sum_result(current_value, "+", display_screen)

        if operator == "-":
            return show_subtraction_result(current_value, "-", display_screen)

        if operator == "/":
            return show_division_result(current_value, "/", display_screen)




def show_division_result(current_value, operator, display_screen):
        
    while True:

        # -----------------------------------
        # 1. Reset with C
        # -----------------------------------
        if operator == "C":
            print("Resetting...")

            display_screen.clear()      # Completely clears the list that shows the operation

            current_value = request_first_number()  # Requests a new initial number
            if current_value is None:  # If the user cancels
                return

            # A new initial operator is requested
            operator = input(
                "Choose operation: \n"
                "+ , - , * , / , = , C (reset) or Exit: "
            )

            # We validate that the operator is valid
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using / by default.")
                operator = "/"

            continue  # Restarts the main loop

        # -----------------------------------
        # 2. End operation
        # -----------------------------------
        if operator == "=":
            print(" ".join(display_screen))  # Shows the entire operation
            print(f"Final result: {current_value}")  # Total result
            return  # Ends the current function

        # -----------------------------------
        # 3. Exit completely
        # -----------------------------------
        if operator == "Exit":
            print("End of program")
            sys.exit()  # Closes the program

        # -----------------------------------
        # 4. Request number
        # -----------------------------------
        try:
            num_2 = input("Enter a number: ")

            # Validations to avoid letters, strange symbols or spaces
            if (
                not num_2.strip()  # empty or spaces
                or any(c in '+-*/=!@#$%^&()[];:{}",<>?' for c in num_2)  # prohibited symbols
                or num_2[0].isspace()  # starts with space
                or not all(c.isdigit() or c == '.' for c in num_2)  # only digits and period
            ):
                raise ValueError(
                    "You can only enter numbers. Letters, signs, or empty spaces are not allowed."
                )

            next_value = float(num_2)  # Convert to number

        except ValueError as e:
            # If there was an error in the entered number
            print("Error:", e)

            # An operator is requested to decide what to do after the error
            operator = input(
                "Enter operator (+, -, *, /, =, C, Exit) or Enter to try again with addition: "
            )

            if operator == "":
                operator = "/"  # By default continues dividing

            # If enters C must reset at the top
            if operator == "C":
                continue

            # Normal operator validation
            if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
                print("Invalid operator. Using / by default.")
                operator = "/"

            continue  # Goes back to request number

        # -----------------------------------
        # 5. Add correct operator to the screen
        # -----------------------------------
        if not display_screen:  
            # If it's the first operation, the initial value is added
            display_screen.append(str(current_value))

        # If the last element is NOT an operator, the current operator is added
        if display_screen[-1] not in ["+", "-", "*", "/"]:
            display_screen.append(operator)

        # The entered number is added
        display_screen.append(str(next_value))

        # -----------------------------------
        # 6. Perform operation 
        # -----------------------------------
        current_value /= next_value  # Real division

        # -----------------------------------
        # 7. Show partial result
        # -----------------------------------
        print("******************************")
        print(" ".join(display_screen))  # Shows everything entered
        print(f"Partial result: {current_value}")  # Prints partial result
        print("******************************")

        # -----------------------------------
        # 8. Request next operator
        # -----------------------------------
        operator = input(
            "Enter operator (+, -, *, /, =, C, Exit):  "
        )

        # Validation of the entered operator
        if operator not in ["+", "-", "*", "/", "=", "C", "Exit"]:
            print("Invalid operator. Continuing with division by default.")
            operator = "/"  # Continues dividing by default

        # Delegations to other functions according to the chosen operator
        if operator == "+":
            return show_sum_result(current_value, "+", display_screen)

        if operator == "-":
            return show_subtraction_result(current_value, "-", display_screen)

        if operator == "*":
            return show_multiplication_result(current_value, "*", display_screen)

        # If it doesn't enter here, the loop will continue and handle =, C, Exit at the top



def main():
    # List that will store the operation displayed on screen
    display_screen = []

    # The first number is requested
    first_number = request_first_number()

    # If the user canceled (None), everything ends
    if first_number is None:
        return

    # The menu is shown and the initial operator is obtained + the updated list
    option, display_screen = show_menu(first_number, display_screen)

    # If option is None, execution ended in the menu
    if option is None:
        return

    # -------------------------------------------------------------
    # Choose the correct function depending on the entered operator
    # -------------------------------------------------------------
    if option == "+":
        show_sum_result(first_number, option, display_screen)

    elif option == "-":
        show_subtraction_result(first_number, option, display_screen)

    elif option == "*":
        show_multiplication_result(first_number, option, display_screen)

    elif option == "/":
        show_division_result(first_number, option, display_screen)

    # If the user put "=", we simply show the result
    elif option == "=":
        print(f"Final result: {first_number}")

    # Reset everything from zero
    elif option == "C":
        main()

    # Close program
    elif option == "Exit":
        print("End of program")
        sys.exit()

main()