"""
This file contains the program's entry point.
Here we control the main flow and user interaction.
"""

from menu import menu_option  # Function that displays the menu and returns the chosen option
from actions import add_student, show_students, show_students_top, get_class_average, show_failed_students, delete_students
# Import of all functions related to student operations

from data import export_students_data, import_students_data
# Import of functions to handle CSV files (export and import)


def main():
    # Main list where all students are stored
    students = []

    # Main program loop (runs until user decides to exit)
    while True:

        # Get the option chosen by the user from the menu
        option = menu_option()

        # Execute the corresponding function based on the option

        if option == 1:
            # Add one or multiple students to the list
            add_student(students)

        elif option == 2:
            # Show all registered students
            show_students(students)

        elif option == 3:
            # Show the top 3 students with the best performance
            show_students_top(students)

        elif option == 4:
            # Show the average score for each student
            get_class_average(students)

        elif option == 5:
            # Show failed students (any grade below 60)
            show_failed_students(students)

        elif option == 6:
            # Delete a student from the list
            delete_students(students)

        elif option == 7:
            # Export the student list to a CSV file
            export_students_data(students)

        elif option == 8:
            # Import students from a CSV file
            import_students_data(students)

        elif option == 0:
            # Exit the program
            print("Goodbye!")
            break


# Program entry point
# This block ensures main() only runs when the file is executed directly
if __name__ == "__main__":
    main()