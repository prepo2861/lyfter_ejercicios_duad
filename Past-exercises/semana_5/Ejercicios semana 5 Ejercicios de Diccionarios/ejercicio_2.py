"""
1. Cree un programa que cree un diccionario usando dos listas del mismo tamaño, usando una para sus keys, y la otra para sus values.
    1. Ejemplos:
    2. `list_a = [’first_name’, ‘last_name’, ‘role’]`
    `list_b = [’Alek’, ‘Castillo’, ‘Software Engineer’]`
    → `{’first_name’: ‘Alek’, ‘last_name’: ‘Castillo’, ‘role’: ‘Software Engineer’}`
"""

def exercise_3():

    # We will name the 2 lists that will be used
    list_a = ["first_name", "last_name", "role"]
    list_b = ["Roberto", "Ortega", "Software Engineer"]

    # We create the dictionary
    new_list = {}

    for i in range(len(list_a)):  # We make a for loop to go through each element of the list
        new_list[list_a[i]] = list_b[i]  # We assign each key from list_a to the corresponding value in list_b

    print(new_list)  # We show the result

exercise_3()
