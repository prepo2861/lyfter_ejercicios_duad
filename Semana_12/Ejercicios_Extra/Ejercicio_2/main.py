# This is the main file. It controls the users system menu

from users import AdminUser, RegularUser
from menu import menu_option


def main():

    # Keep the program running until the user chooses to exit
    while True:

        # Display the menu and get the selected option
        option = menu_option()

        # Create an AdminUser object
        if option == 1:

            name = input("Enter the admin name: ")

            user = AdminUser(name)

        # Create a RegularUser object
        elif option == 2:

            name = input("Enter the regular user name: ")

            user = RegularUser(name)

        # Exit the program
        elif option == 0:

            print("Goodbye!")
            break

        # Display the user's information
        print(f"\nUser: {user.name}")
        print(f"Role: {user.get_role()}")

        # Ask the user for a permission to verify
        permission = input(
            "Enter a permission (read/write/delete): "
        ).lower()

        # Check if the user has the requested permission
        if user.has_permission(permission):

            print("Access granted.")

        else:

            print("Access denied.")

        # Pause before showing the menu again
        input("\nPress Enter to return to menu...")


# Run the program only when this file is executed directly
if __name__ == "__main__":

    main()