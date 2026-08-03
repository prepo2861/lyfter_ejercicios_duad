"""
Cree una función que imprima “Hola, [nombre]” dos veces:
Cree un decorador @repeat_twice que haga que la función decorada se ejecute dos veces seguidas, con los mismos argumentos
Ejemplo:
Salida:

"Hola, Jeanca"

"Hola, Jeanca"

"""

# Decorator that executes a function twice
def repeat_twice(function):

    # Wrapper receives all arguments passed to the decorated function
    def wrapper(*args):

        # Execute the function for the first time
        function(*args)

        # Execute the function for the second time
        function(*args)

    # Return the wrapper function
    return wrapper


# Apply the repeat_twice decorator to the saludo function
@repeat_twice
def saludo(nombre):

    # Print a greeting using the provided name
    print(f"Hola, {nombre}")


# Store the user's name
user = "Roberto"

# Call the decorated function
saludo(user)

