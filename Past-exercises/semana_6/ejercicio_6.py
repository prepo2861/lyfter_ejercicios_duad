"""
6. Cree una función que acepte un string con palabras separadas por un guión y retorne un string igual pero ordenado alfabéticamente.
    1. Hay que convertirlo a lista, ordenarlo, y convertirlo nuevamente a string.
    2. “python-variable-funcion-computadora-monitor” → “computadora-funcion-monitor-python-variable”

"""

def sort_string():
    my_string = "python-variable-function-computer-monitor"

    print(f"Original list = {my_string}")

    # Convert the string into a list separated by '-'
    my_list = my_string.split("-")

    # Manual sorting
    # Traverse the list
    for i in range(len(my_list)):
        min_index = i

            # Compare the word from the traversal with the rest of the list
        for j in range(i + 1, len(my_list)):
            if my_list[j] < my_list[min_index]:
                min_index = j
                
        # Swap if we find a smaller one
        my_list[i], my_list[min_index] = my_list[min_index], my_list[i]

    # Convert the sorted list back into a string
    my_new_string = "-".join(my_list)
    print(f"Sorted list = {my_new_string}")

sort_string()







