"""
1. Experimente haciendo sumas entre distintos tipos de datos y apunte los resultados.
    1. Si le salen errores, **no se asuste.** Lealos e intente comprender qué significan.
    *Los errores son oportunidades de aprendizaje.*
    2. Por ejemplo:
        1. string + string → ?
        2. string + int → ?
        3. int + string → ?
        4. list + list → ?
        5. string + list → ?
        6. float + int → ?
        7. bool + bool → ?
"""

def data():

    #1. string + string → ?
    #Let's input 2 string values for the first example
    string_1 = "Hello"
    string_2 = "World"
    result_1 = string_1 + string_2

    print(result_1) #The result of this is HelloWorld. The phrase is joined without spaces

    #2. string + int → ?
    #Let's input an int value for the examples
    number_1 = 2025
    #result_2 = string_1 + number_1
    #print(result_2) # This would give the following error: TypeError: can only concatenate str (not "int") to str. This is because the int is not converted to string to be read with the string
    result_2 = string_1 + str(number_1)
    print(result_2) #By using str(number_1) we convert the int to string so it can be concatenated

    #3. int + string → ?
    #result_3 = number_1 + string_1
    #print(result_3) # This shows the error: TypeError: unsupported operand type(s) for +: 'int' and 'str'. This means Python doesn't know how to combine an int and a string with the + operator
    result_3 = string_1 + str(number_1)
    print(result_3) #We can use the same method as before and convert the int to string to concatenate

    #4. list + list → ?
    #Let's name two lists with their values
    list_1 = [1,2,3]
    list_2 = [4,5,6]
    result_4 = list_1 + list_2
    print(result_4) #Here we can add two lists without problems

    #5. string + list → ?
    #result_5 = list_1 + string_1
    #print(result_5) # This example gives the error: TypeError: can only concatenate list (not "str") to list because a string and a list are different types.

    #6. float + int → ?
    #Let's create a float for this example
    decimal_1 = 3.14
    result_6 = number_1 + decimal_1
    print(result_6) #When combining an int with a float, the result is always a float. The int is automatically converted to float.

    #7. bool + bool → ?
    #Let's create two bools for the example
    bool_1 = True
    bool_2 = False
    result_7 = bool_1 + bool_2
    print(result_7) #In Python booleans are represented as ints. True equals 1 and False equals 0. So the result will be 1 when added.

data()

