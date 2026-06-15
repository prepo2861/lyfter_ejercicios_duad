"""
3. Cree un programa que intercambie el primer y ultimo elemento de una lista. Debe funcionar con listas de cualquier tamaño.
    1. Ejemplos:
    2. `my_list = [4, 3, 6, 1, 7]` → `[7, 3, 6, 1, 4]`
"""

def exercise_3():

    my_list = [4, 3, 6, 1, 7]
    print("Original list:", my_list)

    # We check that it has at least 2 elements
    if len(my_list) < 2:
        print("The list is too short to swap elements")
    else:
        # We swap the first and last element
        my_list[0], my_list[-1] = my_list[-1], my_list[0]

    print("New list:", my_list)

exercise_3()
