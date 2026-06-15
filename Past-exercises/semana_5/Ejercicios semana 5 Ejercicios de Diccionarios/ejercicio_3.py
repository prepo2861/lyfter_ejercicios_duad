"""
2. Cree un programa que use una lista para eliminar keys de un diccionario.
    1. Ejemplos:
    2. `list_of_keys = [’access_level’, ‘age’]`
    `employee = {’name’: ‘John’, ‘email’: ‘john@ecorp.com’, ‘access_level’: 5, ‘age’: 28}`
    → `{’name’: ‘John’, 'email’: ‘john@ecorp.com’}`

"""

def exercise_3():

    list_of_keys = ["access_level", "age"]  
    
    employee = {"name": "John",
                "email": "john@ecorp.com",
                "access_level": 5,
                "age": 28
                }
    
    print(employee)

    for key in list_of_keys:  # Loop through the dictionary.
        deleted_item = employee.pop(key)  # Delete the key that is in list_of_keys
    
    print(employee)  # Show the result
    print(deleted_item)  # Show the deleted keys

exercise_3()
