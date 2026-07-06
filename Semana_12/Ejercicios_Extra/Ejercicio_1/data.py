"""
This file contains all the logic for employee data export and import.
"""

import csv
import os

from employee import Employee


def export_employee(employees):
    """
    Exports the employee list to a CSV file.
    Allows the user to specify the filename and overwrite it if it already exists.
    """

    if not employees:
        print("*************************************")
        print("No employees registered.")
        print("*************************************")
        return

    filename = input(
        "Enter the name of the CSV file to export or type 'cancel' to exit: "
    ).strip()

    if filename.lower() == "cancel":
        print("*************************************")
        print("You will return to the main menu")
        print("*************************************")
        return

    if not filename.endswith(".csv"):
        filename += ".csv"

    if os.path.exists(filename):
        answer = input("The file already exists. Overwrite? (y/n): ")

        if answer.lower() != "y":
            print("Export cancelled.")
            return

    with open(filename, "w", encoding="utf-8", newline="") as file:

        writer = csv.writer(file)

        writer.writerow([
            "Name",
            "Salary"
        ])

        for employee in employees:
            writer.writerow([
                employee.name,
                employee.salary
            ])

    print(f"File '{filename}' created successfully.")


def import_employee(employees):
    """
    Imports employees from a CSV file and adds them to the employee list.
    """

    if employees:
        print("Warning: Existing data will be extended.")
    else:
        print("Warning: No CSV file has been uploaded yet.")

    while True:

        filename = input(
            "Enter the name of the CSV file to import or type 'cancel' to exit: "
        ).strip()

        if filename.lower() == "cancel":
            print("*************************************")
            print("You will return to the main menu")
            print("*************************************")
            return

        if not filename.endswith(".csv"):
            filename += ".csv"

        try:

            with open(filename, "r", encoding="utf-8") as file:

                reader = csv.DictReader(file)

                for row in reader:

                    employee = Employee(
                        row["Name"],
                        float(row["Salary"])
                    )

                    employees.append(employee)

            print("*************************************")
            print(f"The file '{filename}' has been loaded!")
            print("*************************************")

            input("\nPress Enter to return to menu...")
            return

        except FileNotFoundError:
            print(f"Error: file '{filename}' does not exist.")

        except ValueError as e:
            print(f"Error: {e}")