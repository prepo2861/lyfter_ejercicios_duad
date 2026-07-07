# This is the main file. It controls the employee system menu

from menu import menu_option
from employee import EmployeeManager
from data import (import_employee, export_employee)


def main():

    manager = EmployeeManager()

    while True:

        option = menu_option()

        if option == 1:
            manager.add_employee()

        elif option == 2:
            manager.show_employees()

        elif option == 3:
            manager.promote_employee()

        elif option == 4:
            manager.delete_employee()

        elif option == 5:
            export_employee(manager.employees)

        elif option == 6:
            import_employee(manager.employees)

        elif option == 0:
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()






