# All menu option logic is handled here
def menu_option(menu=8):

    # Infinite loop until the user enters a valid option
    while True:
        try:
            # Ask the user to choose a menu option
            option = int(input(
                "****************************************\n"
                "Please choose the following options\n"
                "***************************************\n"
                "1- Add student\n"
                "2- Show student info\n"
                "3- Show top 3 best student rank\n"
                "4- Show student average score\n"
                "5- Show failed students\n"
                "6- Delete student \n"
                "7- Export data to csv\n"
                "8- Import data from csv \n"
                "0- Exit\n"
                "**************************************\n"
                "Option: "
            ))

            # Validation: option must be within the allowed range (0 to menu)
            if option < 0 or option > menu:
                # If outside the range, raise an error
                raise ValueError

            # If the option is valid, return it to the main program
            return option

        except ValueError:
            # Error handling if user enters invalid value (text or number out of range)
            print("Error: please choose only options 0 to 8")