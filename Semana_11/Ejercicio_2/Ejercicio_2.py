"""
Cree una clase de Bus con:
Un atributo de max_passengers.
Un método para agregar pasajeros uno por uno 
(que acepte como parámetro una instancia de la clase Person vista en la lección). 
Este solo debe agregar pasajeros si lleva menos de su máximo. Sino, debe mostrar un mensaje de que el bus está lleno.

"""

class Bus:

    # Constructor of the Bus class
    def __init__(self):

        # Keep asking until the user enters a valid capacity
        while True:

            try:

                # Request the maximum number of passengers
                self.max_passengers = int(
                    input(
                        "Please select the max capacity of passengers: "
                    )
                )

                # Validate that the capacity is greater than zero
                if self.max_passengers <= 0:
                    raise ValueError

                # Exit the loop if the value is valid
                break

            except ValueError:

                # Display an error message if the input is invalid
                print(
                    "Error, you must enter a valid positive number."
                )

        # List used to store all passengers currently on the bus
        self.passengers = []

    # Method to add a passenger to the bus
    def add_passenger(self, person):

        # Check if there is still available space
        if len(self.passengers) < self.max_passengers:

            # Add the person to the passengers list
            self.passengers.append(person)

            # Return True indicating the person was able to get in
            return True

        # If the bus is full, return False
        return False

    # Method to remove a passenger from the bus
    def delete_passenger(self):

        # Check if the bus is empty
        if not self.passengers:
            print("There are no passengers to get off the bus.")
        else:

            # Remove the last passenger added
            removed = self.passengers.pop()

            # Show information about the removed passenger
            print(f"{removed.name} has gotten off the bus!")
            print(f"There are now {len(self.passengers)} passengers on the bus.")


class Person:

    # Constructor of the Person class
    def __init__(self, name):

        # Save the person's name
        self.name = name

def main():

        # Create an instance of the bus
    my_bus = Bus()

    # List of valid options for the user
    display_options = ["y", "n", "exit"]

    # Main loop of the program
    while True:

        try:

            

            # Ask if they want to add a new person
            add_person_option = input(
                "Do you want to add a new person to the bus? Y/N: "
            ).lower()

            # Verify that the entered option is valid
            if add_person_option not in display_options:
                raise ValueError

            # If the user wants to add a person
            if add_person_option == "y":

                # Ask for the person's name
                name = input("Enter the person's name: ")

                # Validate that the name:
                # - is not empty
                # - does not contain numbers
                if (
                    not name.strip()
                    or any(char.isdigit() for char in name)
                ):
                    raise ValueError

                # Create an instance of Person
                person_1 = Person(name)

                # Try to add the person to the bus
                result = my_bus.add_passenger(person_1)

                # If able to get on the bus
                if result:
                    print("**********************************************")
                    print(
                        f"Person {person_1.name} has gotten on the bus."
                    )

                    # Calculate available seats remaining
                    print(
                        f"There are "
                        f"{my_bus.max_passengers - len(my_bus.passengers)} "
                        f"available seats left."
                    )
                    print("**********************************************")

                # If the bus is full
                else:
                    print("**********************************************")
                    print("The bus is full!")
                    print("**********************************************")

            # If the user does not want to add passengers
            elif add_person_option == "n":

                print("**********************************************")
                print("No passengers will be added at this time.")

                # Show available seats
                print(
                    f"There are "
                    f"{my_bus.max_passengers - len(my_bus.passengers)} "
                    f"seats available."
                )
                print("**********************************************")

                # End the program
                break

            # Ask if they want to remove a passenger
            delete_person_option = input(
                "Do you want to remove a person from the bus? "
                "Y/N or type 'exit': "
            ).lower()

            # Verify that the entered option is valid
            if delete_person_option not in display_options:
                raise ValueError

            # If they want to remove a passenger
            if delete_person_option == "y":

                # Execute the method to remove passengers
                my_bus.delete_passenger()

            # If they do not want to remove passengers
            elif delete_person_option == "n":

                print("**********************************************")

                # Show the current number of passengers
                print(
                    f"There are currently "
                    f"{len(my_bus.passengers)} passengers on the bus."
                )
                print("**********************************************")

            # If they want to exit the program
            elif delete_person_option == "exit":

                print("**********************************************")
                print("No passengers will be added at this time.")

                # Show available seats before exiting
                print(
                    f"There are "
                    f"{my_bus.max_passengers - len(my_bus.passengers)} "
                    f"seats available."
                )
                print("**********************************************")

                # End the program
                break

        # Catch validation errors
        except ValueError:

            print("**********************************************")
            print(
                "Error: you can only enter the values "
                "allowed by the system."
            )
            print("**********************************************")

# Execute the main function
if __name__ == "__main__":

    main()




        