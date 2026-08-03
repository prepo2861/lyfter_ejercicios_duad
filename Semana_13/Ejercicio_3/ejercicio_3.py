"""
Cree una clase de User que:
Tenga un atributo de date_of_birth.
Tenga un property de age.
Luego cree un decorador para funciones que acepten un User como 
parámetro que se encargue de revisar si el User es mayor de edad y arroje una excepción de no ser así.

"""
from datetime import date


class User:

    def __init__(self, date_birth):
        # Store the user's date of birth
        self.date_birth = date_birth

    @property
    def age(self):

        # Get today's date
        today = date.today()

        # Calculate the user's age based on the years
        age = today.year - self.date_birth.year

        # Check if the user has already had their birthday this year
        if today.month > self.date_birth.month:
            pass

        # If the current month is the same as the birth month,
        # we need to compare the days
        elif today.month == self.date_birth.month:

            # The user already had their birthday
            if today.day >= self.date_birth.day:
                pass

            # The user has not had their birthday yet
            else:
                age = age - 1

        # The birth month has not arrived yet
        else:
            age = age - 1

        # Return the calculated age
        return age


# Decorator that checks if the User is of legal age
def show_age(function):

    # Wrapper receives a User object
    def wrapper(user):

        # Check if the user is 18 or older
        if user.age >= 18:
            pass

        # If the user is under 18, raise an exception
        else:
            raise ValueError("You are underage!")

        # Execute the decorated function
        result = function(user)

        # Return the result of the decorated function
        return result

    # Return the wrapper function
    return wrapper


# Apply the show_age decorator to this function
@show_age
def show_result(user):

    # This message is only displayed if the user is 18 or older
    print("Welcome, you are legal!!")


# Create a User object with a date of birth
user = User(date(1992, 6, 28))

# Call the decorated function
show_result(user)







