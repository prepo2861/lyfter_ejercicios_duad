"""
Cree un decorador @requires_login que:
Verifique si la variable global user_logged_in es True
Si no lo es, debe lanzar una excepción "Usuario no autenticado"
Si lo es, la función decorada se ejecuta normalmente
Ejemplo:
Entrada:

user_logged_in = False

@requires_login
def view_profile():
    print("Mostrando perfil del usuario")

"""


# Global variable that indicates whether the user is authenticated
user_logged_in = False


# Decorator that checks if the user is authenticated
def requires_login(function):

    # Wrapper function that controls access to the decorated function
    def wrapper():

        # Check if the user is logged in
        if user_logged_in:

            # Execute the decorated function
            result = function()

            # Return the result of the decorated function
            return result

        # If the user is not logged in, raise an exception
        else:
            raise ValueError("User not authenticated")

    # Return the wrapper function
    return wrapper


# Apply the requires_login decorator to the view_profile function
@requires_login
def view_profile():

    # Display the user's profile
    print("Mostrando perfil del usuario")


# Call the decorated function
view_profile()
