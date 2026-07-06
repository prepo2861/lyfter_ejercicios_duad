# This is the main file. It controls the Vehicle Information System.

from menu import menu_option
from vehicle import Motorcycle, Car


def main():

    # Keep the program running until the user chooses to exit
    while True:

        # Display the menu and get the selected option
        option = menu_option()

        # Create and display a Car object
        if option == 1:

            try:

                # Request the car information from the user
                car_name = input("Enter the brand of the Car: ")
                car_year = int(input("Enter the year of the Car: "))
                car_doors = int(
                    input("Enter the number of doors of the Car: ")
                )

                # Create a new Car object
                new_car = Car(
                    car_name,
                    car_year,
                    car_doors
                )

                # Display the vehicle information
                print("*****************************************************")
                print("Vehicle information:")
                print("*****************************************************")
                print(new_car.get_info())
                print("*****************************************************")

                # Pause before showing the menu again
                input("\nPress Enter to continue...")

            # Handle invalid input or validation errors
            except ValueError as e:
                print(f"Error: {e}")

                # Pause before showing the menu again
                input("\nPress Enter to continue...")

        # Create and display a Motorcycle object
        elif option == 2:

            try:

                # Request the motorcycle information from the user
                bike_name = input(
                    "Enter the brand of the Motorcycle: "
                )
                bike_year = int(
                    input("Enter the year of the Motorcycle: ")
                )
                bike_type = input(
                    "Enter the type of the Motorcycle: "
                )

                # Create a new Motorcycle object
                new_bike = Motorcycle(
                    bike_name,
                    bike_year,
                    bike_type
                )

                # Display the vehicle information
                print("*****************************************************")
                print("Vehicle information:")
                print("*****************************************************")
                print(new_bike.get_info())
                print("*****************************************************")

                # Pause before showing the menu again
                input("\nPress Enter to continue...")

            # Handle invalid input or validation errors
            except ValueError as e:
                print(f"Error: {e}")

                # Pause before showing the menu again
                input("\nPress Enter to continue...")

        # Exit the program
        elif option == 0:

            print("Goodbye!")
            break


# Run the program only when this file is executed directly
if __name__ == "__main__":

    main()