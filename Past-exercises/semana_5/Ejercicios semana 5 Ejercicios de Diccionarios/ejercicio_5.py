"""
1. Agrupar empleados por departamento
- Dada una lista de empleados donde cada uno tiene nombre, correo y departamento, cree un diccionario que agrupe los empleados por su departamento

"""


def exercise_5():
    employees = [
        {"name": "Carlos", "email": "carlos@empresa.com", "department": "Sales"},
        {"name": "Ana", "email": "ana@empresa.com", "department": "IT"},
        {"name": "Luis", "email": "luis@empresa.com", "department": "Sales"},
        {"name": "Sofía", "email": "sofia@empresa.com", "department": "HR"},
    ]

    # Create 3 dictionaries to divide the departments
    sales = {}
    it = {}
    hr = {}

    for employee in employees:  # Loop through the list of employees
        
        # Check which department each one belongs to.
        if employee["department"] == "Sales":
            sales[employee["name"]] = employee["email"]  # Add their name as key and email as value to the corresponding dictionary.

        elif employee["department"] == "IT":
            it[employee["name"]] = employee["email"]  # Add their name as key and email as value to the corresponding dictionary.

        elif employee["department"] == "HR":
            hr[employee["name"]] = employee["email"]  # Add their name as key and email as value to the corresponding dictionary.

    # Display result
    print(f"Sales department: {sales}")
    print(f"IT department: {it}")
    print(f"HR department: {hr}")

exercise_5()

