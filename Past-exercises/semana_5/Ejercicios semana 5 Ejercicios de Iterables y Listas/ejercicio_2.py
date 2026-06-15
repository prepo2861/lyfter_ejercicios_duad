"""
2. Cree un programa que itere e imprima un string letra por letra de derecha a izquierda.
    1. Pista: investigue de que otras maneras se puede usar el `range`.
    2. Ejemplos:
    3. `my_string = ‘Pizza con piña’` → 

    a
    ñ
    i
    p
    
    n
    o
    c
    
    a
    z
    z
    i
    p

"""

def exercise_2():

    my_string = "Pizza con piña"
    my_reversed_string = my_string[::-1]  # Reverses the text

    for i in range(len(my_reversed_string)):  # Generates the indices of the text
        print(my_reversed_string[i])  # Prints letter by letter in reverse order

exercise_2()
