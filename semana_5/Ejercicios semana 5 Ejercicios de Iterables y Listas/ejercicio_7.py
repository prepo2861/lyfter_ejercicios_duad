"""
**Cree un programa que verifique si todos los elementos de una lista son positivos**
- Restricciones:
    - No use funciones como `all()`
"""

def exercise_7():

    my_list = []  # We create the empty list

    query = int(input("How many values do you want to enter in the list?: "))  # We ask the user how many numbers they want to enter in the list

    for i in range(query):  # We create a for loop based on what the user has placed in the query variable
        number = int(input(f"Enter the value number {i+1}: "))  # we ask for the numbers

        my_list.append(number)  # we add the values to the list

    for index, values in enumerate(my_list):  # we use enumerate to do the search we need
        if values <= 0:  # we make the condition to check if there are negative numbers or zero in the list
            print(f"There is at least one negative or zero value in the list")  # we show the result
            break
    else:
        print("All values in the list are positive numbers")  # if there are no negative or zero numbers, we show the result

exercise_7()
