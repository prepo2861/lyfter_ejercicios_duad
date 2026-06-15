"""
This file contains all the logic for data export and import.
"""

import csv  # Module for reading and writing CSV files
import os   # Module for validating file existence


def export_students_data(students):
    """
    Exports the student list to a CSV file.
    Allows user to specify filename and overwrite if file already exists.
    """

    # Validation: if no students, nothing to export
    if not students:
        print("*************************************")
        print("No students registered.")
        print("*************************************")
        return

    # Ask user for filename or to cancel
    option = input("Enter the name of the CSV file to export or type 'cancel' to exit: ")

    if option.lower() == "cancel":
        print("*************************************")
        print("You will return to the main menu")
        print("*************************************")
        return

    # Assign entered name (though it will be asked again)
    filename = option

    # Ask again for filename (overwrites previous variable)
    filename = input("Please enter the name of the new file: ").strip()

    # Ensure file has .csv extension
    if not filename.endswith(".csv"):
        filename += ".csv"

    # Check if file already exists
    if os.path.exists(filename):
        answer = input("The file already exists. Overwrite? (y/n): ")

        # If user doesn't confirm, cancel export
        if answer.lower() != "y":
            print("Export cancelled.")
            return

    # Open file in write mode
    with open(filename, "w", encoding="utf-8", newline="") as file:

        writer = csv.writer(file)

        # Write CSV header
        writer.writerow([
            "Name",
            "Class",
            "Spanish",
            "English",
            "Social Studies",
            "Science"
        ])

        # Write each student as a row
        for student in students:
            writer.writerow([
                student["name"],
                student["class"],
                student["spanish_score"],
                student["english_score"],
                student["social_studies_score"],
                student["science_score"]
            ])

    # Success message
    print(f"File '{filename}' created successfully.")


def import_students_data(students):
    """
    Imports students from a CSV file and adds them to the 'students' list.
    """

    # Message depending on whether data is already loaded
    if students:
        print("Warning: Existing data will be extended.")
    else:
        print("Warning: No CSV file has been uploaded yet.")

    # Loop until valid file is loaded or user cancels
    while True:

        # Ask for filename or cancel
        option = input("Enter the name of the CSV file to import or type 'cancel' to exit: ")

        if option.lower() == "cancel":
            print("*************************************")
            print("You will return to the main menu")
            print("*************************************")
            return

        # Assign entered name
        filename = option

        # Ensure .csv extension
        if not filename.endswith(".csv"):
            filename += ".csv"

        try:
            # Open file in read mode
            with open(filename, "r", encoding="utf-8") as file:

                # Use DictReader to read each row as dictionary
                reader = csv.DictReader(file)

                # Loop through each CSV row
                for row in reader:
                    students.append({
                        "name": row["Name"],
                        "class": row["Class"],
                        "spanish_score": float(row["Spanish"]),
                        "english_score": float(row["English"]),
                        "social_studies_score": float(row["Social Studies"]),
                        "science_score": float(row["Science"])
                    })

                # Success message
                print("*************************************")
                print(f"The file '{filename}' has been loaded!")
                print("*************************************")

                input("\nPress Enter to return to menu...")
                return

        except FileNotFoundError:
            # Handle error if file doesn't exist
            print(f"Error: file '{filename}' does not exist.")