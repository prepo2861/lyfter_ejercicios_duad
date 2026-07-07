# All menu option logic is handled here

def menu_option(menu=2):

    # Keep showing the menu until a valid option is entered
    while True:

        try:

            # Display the menu and request an option from the user
            option = int(
                input(
                    "****************************************\n"
                    "Welcome to the Vehicle Information System\n"
                    "Please choose one of the following options\n"
                    "****************************************\n"
                    "1- Create Car\n"
                    "2- Create Motorcycle\n"
                    "0- Exit\n"
                    "****************************************\n"
                    "Option: "
                )
            )

            # Validate that the option is within the allowed range
            if option < 0 or option > menu:
                raise ValueError

            # Return the selected option
            return option

        except ValueError:

            # Display an error message if the option is invalid
            print("****************************************")
            print("Please enter a valid option.")
            print("****************************************")

            # Pause before showing the menu again
            input("\nPress Enter to return to menu...")