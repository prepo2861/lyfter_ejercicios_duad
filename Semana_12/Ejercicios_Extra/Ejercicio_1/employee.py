"""
Cree una clase Employee con los siguientes requisitos:
Atributos privados: _name, _salary
Use @property y @<atributo>.setter para:
Mostrar el nombre y el salario
Validar que el salario nunca sea negativo
Cree un método promote que aumente el salario un porcentaje definido


"""
class Employee:

    # Constructor used to initialize an employee
    def __init__(self, name, salary):

        # Validate that the name is not empty and does not contain numbers
        if (
            not name.strip()
            or any(char.isdigit() for char in name)
        ):
            raise ValueError(
                "Name must contain only letters."
            )

        # Store the employee name as a protected attribute
        self._name = name

        # Use the salary setter to validate the salary
        self.salary = salary

    # Getter for the employee name
    @property
    def name(self):
        return self._name

    # Getter for the employee salary
    @property
    def salary(self):
        return self._salary

    # Setter for the employee salary
    @salary.setter
    def salary(self, value):

        # Validate that the salary is greater than zero
        if value <= 0:
            raise ValueError(
                "Salary must be greater than zero."
            )

        # Store the salary as a protected attribute
        self._salary = value

    # Increase the employee salary by a given percentage
    def promote(self, percentage):

        # Validate that the percentage is within the allowed range
        if percentage <= 0 or percentage > 20:
            raise ValueError(
                "Percentage must be between 1 and 20."
            )

        # Calculate and update the new salary using the setter
        self.salary = (
            self.salary
            + (self.salary * percentage / 100)
        )

        # Return the updated salary
        return self.salary


class EmployeeManager:

    # Constructor used to initialize the employee list
    def __init__(self):

        self.employees = []

    # Add an employee object to the employee list
    def add_employee(self):

        while True:

            try:

                number_of_employees = int(
                    input(
                        "How many employees do you want to register?: "
                    )
                )

                if number_of_employees <= 0:
                    raise ValueError

                break

            except ValueError:

                print(
                    "Please enter a valid number greater than zero."
                )

        for i in range(number_of_employees):

            while True:

                try:

                    name = input(
                        f"Enter the name of employee #{i + 1}: "
                    ).strip()

                    salary = float(
                        input(
                            f"Enter the salary of employee #{i + 1}: "
                        )
                    )

                    employee = Employee(name, salary)

                    for existing_employee in self.employees:

                        if (
                            existing_employee.name.lower()
                            == employee.name.lower()
                        ):
                            raise ValueError(
                                "Employee already exists."
                            )

                    self.employees.append(employee)

                    print(
                        f"{employee.name} added successfully!"
                    )

                    break

                except ValueError as e:

                    print(f"Error: {e}")

    # Display all registered employees
    def show_employees(self):

        # Check if there are no employees registered
        if not self.employees:
            print("-" * 40)
            print("No employees registered.")
            input("\nPress Enter to continue...")
            return

        # Loop through all employees and display their information
        for employee in self.employees:


            print("-" * 40)
            print(
                f"Employee: {employee.name}  \n"
                f"Salary: ${employee.salary:.2f}"
            )

            # Pause execution before returning to the menu
            input("\nPress Enter to continue...")


    def promote_employee(self):

        if not self.employees:
            print("No employees registered.")
            return

        for employee in self.employees:
            print(f"- {employee.name} (${employee.salary:.2f})")

        selection = input(
            "Enter the name of the employee you want to promote: "
        ).strip()

        for employee in self.employees:

            if employee.name.lower() == selection.lower():

                try:
                    percentage = float(
                        input("Enter promotion percentage: ")
                    )

                    employee.promote(percentage)

                    print("-" * 40)
                    print(
                        f"{employee.name} has been promoted!\n"
                        f"New salary: ${employee.salary:.2f}"
                    )
                    print("-" * 40)

                    input("\nPress Enter to return to menu...")
                    return

                except ValueError as e:
                    print(f"Error: {e}")
                    input("\nPress Enter to return to menu...")
                    return

        print("Employee not found.")
        input("\nPress Enter to return to menu...")

    def delete_employee(self):

        if not self.employees:
            print("*************************************")
            print("No employees registered.")
            print("*************************************")
            return

        while True:

            print("\nList of employees:\n")

            for employee in self.employees:
                print(f"- {employee.name} (${employee.salary:.2f})")

            selection = input(
                "\nEnter the name of the employee you want to delete "
                "or type 'cancel' to exit: "
            )

            if selection.lower() == "cancel":
                print("*************************************")
                print("You will return to the main menu")
                print("*************************************")
                return

            if (
                not selection.strip()
                or any(char.isdigit() for char in selection)
                or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in selection)
            ):
                print("Please enter a valid name.")
                continue

            for employee in self.employees:

                if employee.name.lower() == selection.lower():
                    self.employees.remove(employee)

                    print("-" * 40)
                    print(f"The employee {employee.name} has been deleted!")
                    print("-" * 40)
                    break

            else:
                print("-" * 40)
                print("Employee not found.")
                print("-" * 40)

            input("\nPress Enter to return to menu...")
            return

