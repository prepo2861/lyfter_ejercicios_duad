"""
3. Cree una función que retorne la suma de todos los números de una lista.
    1. La función va a tener un parámetro (la lista) y retornar un numero (la suma de todos sus elementos).
    2. [4, 6, 2, 29] → 41

"""

def sum_of_numbers_of_list(list_of_numbers=[4,6,2,29]):  # Create the function that takes a list of numbers as a parameter

    result_with_sum = sum(list_of_numbers)  # We can use sum to get the result of the list. But we're going to use the lyfter method :D

    print(f"The result of the list using sum is: {result_with_sum}")  # Show the result

    sum_result = 0  # Create the variable that will give the result

    for numbers in list_of_numbers:  # Create the traversal of the list
        sum_result += numbers  # Create the sum

    return sum_result  # Return the result

        


result = sum_of_numbers_of_list()  # Call the function
print(f"The result of the list: {result}")  # Show the result




