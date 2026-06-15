# actions.py
# This file contains the logic for all menu options

import csv  # Module for working with CSV files (not used directly in this file)

import csv


class Student:

    # Constructor method used to initialize a student object
    def __init__(
        self,
        student_name,
        student_class,
        spanish_score,
        english_score,
        social_studies_score,
        science_score
    ):

        # Store the student's name
        self.student_name = student_name

        # Store the student's class/group
        self.student_class = student_class

        # Store the student's Spanish score
        self.spanish_score = spanish_score

        # Store the student's English score
        self.english_score = english_score

        # Store the student's Social Studies score
        self.social_studies_score = social_studies_score

        # Store the student's Science score
        self.science_score = science_score

    @staticmethod
    def get_valid_score(subject):
        """
        Requests a valid score between 0 and 100.
        Keeps asking until the user enters a valid number.
        """

        while True:
            try:

                # Ask the user to enter a score
                score = float(input(f"{subject} score (0-100): "))

                # Validate that the score is within the allowed range
                if 0 <= score <= 100:
                    return score

                print("Score must be between 0 and 100.")

            except ValueError:

                # Handle invalid numeric input
                print("Enter a valid number.")

    @staticmethod
    def get_valid_class():
        """
        Requests a valid class from the available class list.
        Keeps asking until the user enters a valid option.
        """

        # List containing all valid classes
        list_of_classes = [
            "1A", "1B", "1C",
            "2A", "2B", "2C",
            "3A", "3B", "3C",
            "4A", "4B", "4C",
            "5A", "5B", "5C",
            "6A", "6B", "6C",
            "7A", "7B", "7C",
            "8A", "8B", "8C",
            "9A", "9B", "9C",
            "10A", "10B", "10C",
            "11A", "11B", "11C"
        ]

        while True:

            # Ask the user to enter a class
            selection = input(
                "Please enter the class (7A to 11C): "
            ).upper()

            # Validate if the class exists in the list
            if selection in list_of_classes:
                return selection

            # Message displayed if the class is invalid
            print("Enter a valid class.")


def add_student(students):
    """
    Allows the user to register one or multiple students.
    Validates names, classes, and scores before saving data.
    """

    # Ask the user how many students will be registered
    while True:
        try:

            number_of_students = int(
                input("How many students do you want to register?: ")
            )

            # Validate that the number is greater than 0
            if number_of_students > 0:
                break

            print("Number must be greater than 0.")

        except ValueError:

            # Handle invalid numeric input
            print("Please enter a valid number.")

    # Loop through the number of students to register
    for i in range(number_of_students):

        while True:

            # Ask for the student's name
            name = input(
                f"Enter name of student #{i+1}: "
            ).strip()

            # Validate that the name is not empty
            # and does not contain numbers or special characters
            if (
                not name.strip()
                or any(char.isdigit() for char in name)
                or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in name)
            ):
                print(
                    "You must enter a valid name without numbers or special characters."
                )
                continue

            # Ask for the student's class
            class_name = Student.get_valid_class()

            # Check if the student already exists in the same class
            if any(
                student.student_name.lower() == name.lower()
                and student.student_class == class_name
                for student in students
            ):
                print("Student already exists in this class.")
                continue

            break

        # Create a new Student object with validated data
        new_student = Student(
            name,
            class_name,
            Student.get_valid_score("Spanish"),
            Student.get_valid_score("English"),
            Student.get_valid_score("Social Studies"),
            Student.get_valid_score("Science")
        )

        # Add the student object to the main student list
        students.append(new_student)

        # Confirmation message
        print("Student added successfully.")


def show_students(students):
    """
    Displays all registered students and their information.
    """

    # Check if there are any registered students
    if not students:
        print("No students registered.")
        return

    # Loop through the student list and display information
    for i, student in enumerate(students, start=1):

        print("-" * 40)
        print(f"Student {i}")

        # Display student personal information
        print(f"Name: {student.student_name}")
        print(f"Class: {student.student_class}")

        # Display student scores
        print(f"Spanish: {student.spanish_score}")
        print(f"English: {student.english_score}")
        print(f"Social Studies: {student.social_studies_score}")
        print(f"Science: {student.science_score}")

    # Pause execution before returning to the menu
    input("\nPress Enter to continue...")

    
def show_failed_students(students):
    """
    Displays students who have at least one subject score below 60.
    """

    # Check if there are any registered students
    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    # Flag used to determine whether any failed students were found
    found = False

    # Loop through all registered students
    for i, student in enumerate(students, start=1):

        # Check if any subject score is below 60
        if any(
            score < 60
            for score in [
                student.spanish_score,
                student.english_score,
                student.social_studies_score,
                student.science_score
            ]
        ):

            found = True

            print("-" * 40)
            print(f"Student {i}")

            # Display student personal information
            print(f"Name: {student.student_name}")
            print(f"Class: {student.student_class}")

            # Display student scores
            print(f"Spanish: {student.spanish_score}")
            print(f"English: {student.english_score}")
            print(f"Social Studies: {student.social_studies_score}")
            print(f"Science: {student.science_score}")

    # Display a message if no failed students were found
    if not found:
        print("-" * 40)
        print("No failed students found.")

    print("-" * 40)

    # Pause execution before returning to the menu
    input("\nPress Enter to return to menu...")


def show_students_top(students, top_n=3):
    """
    Displays the top students based on their average score.
    By default, the function shows the top 3 students.
    """

    # Check if there are any registered students
    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    # Sort students by average score in descending order
    top_students = sorted(
        students,
        key=lambda s: (
            s.spanish_score +
            s.english_score +
            s.social_studies_score +
            s.science_score
        ) / 4,
        reverse=True
    )[:top_n]

    # Display the top-ranked students
    for i, student in enumerate(top_students, start=1):

        # Calculate the student's average score
        avg = (
            student.spanish_score +
            student.english_score +
            student.social_studies_score +
            student.science_score
        ) / 4

        print(
            f"{i}. "
            f"{student.student_name} "
            f"({student.student_class}) "
            f"- Average: {avg:.2f}"
        )

    # Pause execution before returning to the menu
    input("\nPress Enter to return to menu...")


def get_class_average(students):
    """
    Calculates and displays the overall class average
    based on the average score of all registered students.
    """

    # Check if there are any registered students
    if not students:
        print("No students registered.")
        return

    # Variable used to accumulate each student's average score
    total_avg = 0

    # Loop through all students in the list
    for student in students:

        # Calculate the individual average score for the current student
        avg = (
            student.spanish_score +
            student.english_score +
            student.social_studies_score +
            student.science_score
        ) / 4

        # Add the student's average to the total average accumulator
        total_avg += avg

    # Calculate the overall class average
    class_avg = total_avg / len(students)

    # Display the class average formatted to two decimal places
    print(f"Class average: {class_avg:.2f}")

    # Pause execution before returning to the menu
    input("\nPress Enter to return to menu...")


def delete_students(students):
    """
    Allows the user to delete a student from the list by name.
    """

    # Check if there are any registered students
    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    while True:

        print("\nList of students:\n")

        # Display all registered students
        for student in students:
            print(f"- {student.student_name} ({student.student_class})")

        # Ask the user to enter the student name to delete
        selection = input(
            "\nEnter the name of the student you want to delete or type 'cancel' to exit: "
        )

        # Return to the main menu if the user cancels
        if selection.lower() == "cancel":
            print("*************************************")
            print("You will return to the main menu")
            print("*************************************")
            return

        # Validate the entered name
        if (
            not selection.strip()
            or any(char.isdigit() for char in selection)
            or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in selection)
        ):
            print("Please enter a valid name.")
            continue

        # Search for the student and remove it from the list
        for student in students:

            if student.student_name.lower() == selection.lower():

                students.remove(student)

                print("-" * 40)
                print("The student has been deleted!")
                print("-" * 40)

                break

        else:
            # Execute if no matching student is found
            print("-" * 40)
            print("Student not found.")
            print("-" * 40)

        # Exit the loop after the deletion attempt
        break

    # Pause execution before returning to the menu
    input("\nPress Enter to return to menu...")

