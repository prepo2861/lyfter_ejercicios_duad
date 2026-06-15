"""
1. Cree un programa que itere e imprima los valores de dos listas del mismo tamaño al mismo tiempo.
    1. Ejemplos:
    2. `first_list = [’Hay’, ‘en’, ‘que’, ‘iteracion’, ‘indices’, ‘muy’]`
    `second_list = [’casos’, 'los’, ‘la’, ‘por’, ‘es’, ‘util’]` ->
    Hay casos
    en los
    que la
    iteracion por
    indice es
    muy util

"""

def exercise_1():  # We create the function to work on the practice

    # We make the 2 lists requested in the exercise

    first_list = ["Hay", "en", "que", "iteracion", "indices", "muy"]
    second_list = ["casos", "los", "la", "por", "es", "util"]

    # With len we will return the values of the list and with range we make them go from 0 to 5 since both lists have 6 values
    # min() chooses the smallest size (in case one list is shorter).

    for i in range(min(len(first_list), len(second_list))):
        print(first_list[i], second_list[i])  # We show the result

exercise_1()
