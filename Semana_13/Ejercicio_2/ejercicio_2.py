"""
Cree un decorador que se encargue de revisar si 
todos los parámetros de la función que decore son números, y arroje una excepción de no ser así.

"""

def validate_numbers(function):

    # The wrapper receives all arguments passed to the decorated function
    def wrapper(*args):

        # Iterate through every argument received
        for arg in args:

            # Check if the argument is not an integer or a float
            if not isinstance(arg, (int, float)):

                # Stop the execution and raise an exception
                raise ValueError(
                    f"{arg} is not a valid number"
                )

        # If all arguments are valid, execute the original function
        result = function(*args)

        # Return the function result
        return result

    # Return the modified function
    return wrapper


# Applying the decorator to the function
@validate_numbers
def numbers(*args):

    # Display all received numbers
    print(args)

    # Return the arguments
    return args


# Test with valid numbers
numbers(10, 20, 15)


# Test with an invalid value
# This will raise a ValueError because "Hello" is not a number
numbers(10, 20, 15, "Hello")

