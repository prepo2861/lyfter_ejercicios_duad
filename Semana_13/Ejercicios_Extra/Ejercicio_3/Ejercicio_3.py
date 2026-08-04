"""

Cree una función que se llame multiply, la cual obtiene dos valores y los multiplica entre si
A esta función se le debe combinar dos decoradores:
@log_call: imprime el nombre de la función, los argumentos, fecha actual y el retorno
@validate_numbers: revisa que todos los argumentos sean numéricos
Ejemplo:

Entrada:
multiply(3, 4)

Salida:
"func:multiply - args: 3, 4 - [2025-07-17 14:00:00.000000] - Resultado: 12"
"Resultado 12"

"""

from datetime import datetime


# Decorator that validates that all arguments are numbers
def validate_numbers(function):

    # Wrapper receives all positional arguments
    def wrapper(*args):

        # Check every argument
        for arg in args:

            # Raise an exception if the argument is not a number
            if not isinstance(arg, (int, float)):
                raise ValueError(f"{arg} is not a valid number")

        # Execute the original function with the validated arguments
        return function(*args)

    # Return the wrapper function
    return wrapper


# Decorator that logs information about the function execution
def log_call(function):

    # Wrapper receives all positional arguments
    def wrapper(*args):

        # Get the current date and time
        current_date = datetime.now()

        # Execute the original function
        result = function(*args)

        # Print the function name, arguments, date, and result
        print(
            f"func:{function.__name__} - "
            f"args: {args} - "
            f"[{current_date}] - "
            f"Result: {result}"
        )

        # Return the function result
        return result

    # Return the wrapper function
    return wrapper


# Apply both decorators to the multiply function
@log_call
@validate_numbers
def multiply(a, b):

    # Multiply the two numbers
    return a * b


# Call the function
result = multiply(3, 4)

# Display the final result
print(f"Result {result}")
