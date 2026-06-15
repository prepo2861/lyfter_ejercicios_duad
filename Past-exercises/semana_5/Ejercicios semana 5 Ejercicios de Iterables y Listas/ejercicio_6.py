"""
Cree un programa que cuente cuántas veces aparece un número específico en una lista. Pida al usuario una lista de números y otro número a buscar

"""

def exercise_6():

    my_list = []  # We create the empty list

    query = int(input("How many values do you want to enter in the list?: "))  # We ask the user how many numbers they want to enter in the list

    for i in range(query):  # We create a for loop based on what the user has placed in the query variable
        number = int(input(f"Enter the value number {i+1}: "))  # we ask for the numbers

        my_list.append(number)  # We add them to the list

    search = int(input("Which number from the list do you want to search for?: "))  # We make the query for the number they want to search in the list

    result = my_list.count(search)  # We perform the search

    print(f"The entered list is as follows: {my_list}, and the number {search} appears {result} times")  # we show the result

exercise_6()
