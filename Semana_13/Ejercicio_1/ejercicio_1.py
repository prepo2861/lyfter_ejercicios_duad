"""
Cree un decorador que haga print de los parámetros y retorno de la función que decore.

"""

def log_function_data(function):

    # The wrapper receives the same parameters as the original function
    def wrapper(a, b):

        # Display the arguments received by the decorated function
        print(f"Parameters received: a = {a}, b = {b}")

        # Execute the original function and store the returned value
        result = function(a, b)

        # Display the value returned by the function
        print(f"Function return value: {result}")

        # Return the original result
        return result

    # Return the modified function
    return wrapper


# Applying the decorator to the function
@log_function_data
def sum_numbers(a, b):

    # Return the addition result
    return a + b


# Calling the decorated function
result = sum_numbers(10, 15)

# Display the final result returned by the function
print(f"Final result: {result}")

