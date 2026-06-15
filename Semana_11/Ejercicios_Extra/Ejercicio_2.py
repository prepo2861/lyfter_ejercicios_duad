"""
Cree una clase base Animal y dos clases hijas Dog y Cat:
Animal debe tener nombre y método speak() que retorne "Hace un sonido"
Dog debe sobrescribir speak() para decir "Guau"
Cat debe sobrescribir speak() para decir "Miau"

"""

# Base class representing a generic animal
class Animal:

    # Constructor used to initialize the animal's name
    def __init__(self, name):
        self.name = name

    # Generic sound method
    def speak(self):
        return "Makes a sound"


# Dog class that inherits from Animal
class Dog(Animal):

    # Override the speak method
    def speak(self):
        return "Guau"


# Cat class that inherits from Animal
class Cat(Animal):

    # Override the speak method
    def speak(self):
        return "Miau"


# Keep asking for input until valid names are entered
while True:

    try:

        # Ask the user for the dog's name
        dog_name = input("Please enter the name of the dog: ")

        # Validate that the name is not empty and contains
        # only alphabetic characters
        if (
            not dog_name.strip()
            or any(char.isdigit() for char in dog_name)
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in dog_name)
        ):
            raise ValueError("Invalid dog name.")

        # Create a Dog object
        dog = Dog(dog_name)

        # Ask the user for the cat's name
        cat_name = input("Please enter the name of the cat: ")

        # Validate that the name is not empty and contains
        # only alphabetic characters
        if (
            not cat_name.strip()
            or any(char.isdigit() for char in cat_name)
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in cat_name)
        ):
            raise ValueError("Invalid cat name.")

        # Create a Cat object
        cat = Cat(cat_name)

        # Exit the loop if both names are valid
        break

    except ValueError as e:

        # Display the validation error message
        print("Error:", e)


# Display each animal's name and the sound it makes
print(f"{dog.name} makes {dog.speak()} 🐕")
print(f"{cat.name} makes {cat.speak()}🐈")

   


            
        