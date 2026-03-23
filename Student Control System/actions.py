# actions.py
# This file contains the logic for all menu options

import csv  # Module for working with CSV files (not used directly in this file)


def get_valid_score(subject):
    """
    Requests a valid score between 0 and 100 for the specified subject.
    Keeps asking until the user enters a valid value.
    """
    while True:
        try:
            # Ask user for the score
            score = float(input(f"{subject} score (0-100): "))

            # Validate that the score is within the allowed range
            if 0 <= score <= 100:
                return score
            else:
                print("Score must be between 0 and 100.")

        except ValueError:
            # Handle case where user doesn't enter a number
            print("Enter a valid number.")


def get_valid_class(classes):
    """
    Requests a valid class from the defined list.
    Keeps asking until the user enters a correct class.
    """
    while True:
        try:
            # List of valid classes
            list_of_classes = [
                "1A", "1B","1C",
                "2A","2B","2C",
                "3A","3B","3C",
                "4A", "4B", "4C",
                "5A","5B", "5C",
                "6A","6B","6C",
                "7A","7B","7C",
                "8A","8B","8C",
                "9A","9B","9C",
                "10A","10B","10C",
                "11A", "11B", "11C"
            ]

            # Ask user for class and convert to uppercase
            selection = input(f"please enter the class: Must be 7A to 11C: ").upper()

            # Validate if class is in the list
            if selection not in list_of_classes:
                raise ValueError
            else:
                return selection

        except ValueError:
            print("Enter a valid class")


def add_student(students):
    """
    Allows adding one or multiple students to the 'students' list.
    Validates name, class, and scores before saving.
    """

    # Ask how many students to register
    while True:
        try:
            number_of_students = int(input("Please enter the number of students you want to register: "))

            # Validation: must be greater than 0
            if number_of_students <= 0:
                print("Number must be greater than 0.")
                continue

            break

        except ValueError:
            print("Please enter a valid number.")

    # Loop to register each student
    for i in range(number_of_students):

        while True:
            # Ask for name and class
            name = input(f"Enter name of student #{i+1}: ")
            class_name = get_valid_class("Class")

            # Name validation
            if (
                not name.strip()
                or any(char.isdigit() for char in name)
                or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in name)
            ):
                print("You must enter a valid name without numbers or special characters.")
                continue

            # Duplicate validation (name + class)
            if any(student["name"].lower() == name.lower() and student["class"] == class_name for student in students):
                print(f"The name {name} is already in this class. Please enter another name.")
                continue

            break

        # Create student dictionary
        student = {
            "name": name,
            "class": class_name,
            "spanish_score": get_valid_score("Spanish"),
            "english_score": get_valid_score("English"),
            "social_studies_score": get_valid_score("Social studies"),
            "science_score": get_valid_score("Science")
        }

        # Add to main list
        students.append(student)

        print(f"Student #{i+1} added successfully.")


def show_students(students):
    """
    Displays all registered students with their data.
    """

    # Validation: empty list
    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    # Loop through students
    for i, student in enumerate(students, start=1):

        print("-" * 40)
        print(f"Student {i}")
        print(f"Name: {student['name']}")
        print(f"Class: {student['class']}")
        print(f"Spanish: {student['spanish_score']}")
        print(f"English: {student['english_score']}")
        print(f"Social Studies: {student['social_studies_score']}")
        print(f"Science: {student['science_score']}")

    print("-" * 40)

    # Pause to return to menu
    input("\nPress Enter to return to menu...")


def show_failed_students(students):
    """
    Shows students who have at least one score below 60.
    """

    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    found = False  # Flag to check if any failed students exist

    for i, student in enumerate(students, start=1):

        # Check if any subject is below 60
        if any(score < 60 for score in [
            student['spanish_score'],
            student['english_score'],
            student['social_studies_score'],
            student['science_score']
        ]):

            found = True

            print("-" * 40)
            print(f"Student {i}")
            print(f"Name: {student['name']}")
            print(f"Class: {student['class']}")
            print(f"Spanish: {student['spanish_score']}")
            print(f"English: {student['english_score']}")
            print(f"Social Studies: {student['social_studies_score']}")
            print(f"Science: {student['science_score']}")

    # If no failed students found
    if not found:
        print("-" * 40)
        print("No failed students found.")

    print("-" * 40)

    input("\nPress Enter to return to menu...")


def show_students_top(students, top_n=3):
    """
    Shows the top 'top_n' students based on their average.
    """

    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    # Sort students by average (highest to lowest)
    top_students = sorted(
        students,
        key=lambda s: (
            s["spanish_score"] +
            s["english_score"] +
            s["social_studies_score"] +
            s["science_score"]
        ) / 4,
        reverse=True
    )[:top_n]

    # Display top students
    for i, student in enumerate(top_students, start=1):
        avg = (
            student["spanish_score"] +
            student["english_score"] +
            student["social_studies_score"] +
            student["science_score"]
        ) / 4

        print(f"{i}. {student['name']} ({student['class']}) - Average: {avg:.2f}")

    input("\nPress Enter to return to menu...")


def get_class_average(students):

    # Check if the list is empty
    if not students:
        print("No students registered.")
        return

    # Variable to accumulate the average of each student
    total_avg = 0

    # Loop through each student in the list
    for student in students:

        # Calculate the individual average for the student
        avg = (
            student["spanish_score"] +
            student["english_score"] +
            student["social_studies_score"] +
            student["science_score"]
        ) / 4

        # Add the student's average to the total
        total_avg += avg

    # Calculate the overall class average
    class_avg = total_avg / len(students)

    # Display the result formatted to 2 decimal places
    print(f"Class average: {class_avg:.2f}")

    # Pause execution to allow the user to read the result
    input("\nPress Enter to return to menu...")


def delete_students(students):
    """
    Allows deleting a student from the list by name.
    """

    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    while True:

        print("\nList of students:\n")

        # Show all available students
        for student in students:
            print(f"- {student['name']} ({student['class']})")

        # Ask for name to delete
        selection = input("\nEnter the name of the student you want to delete or type 'cancel' to exit: ")

        if selection.lower() == "cancel":
            print("*************************************")
            print("You will return to the main menu")
            print("*************************************")
            return

        # Name validation
        if (
            not selection.strip()
            or any(char.isdigit() for char in selection)
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in selection)
        ):
            print("Please enter a valid name.")
            continue

        # Search and delete student
        for student in students:
            if student["name"].lower() == selection.lower():
                students.remove(student)
                print("-" * 40)
                print("The student has been deleted!")
                print("-" * 40)
                break
        else:
            # Executes if student not found
            print("-" * 40)
            print("Student not found.")
            print("-" * 40)

        break  # Exit loop after deletion attempt

    input("\nPress Enter to return to menu...")