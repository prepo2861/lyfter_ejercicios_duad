"""
4. Cree un programa que elimine todos los números impares de una lista.
    1. Ejemplos:
    2. `my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]` → `[2, 4, 6, 8]`

"""

def exercise_4():  # we create the function

    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]  # we create the list
    print(f"Original list: {my_list}")

    my_list[:] = [x for x in my_list if x % 2 == 0]  # It goes through the list and at the same time applies the condition for even and odd numbers

    print(f"New list: {my_list}")  # Shows the result

exercise_4()
