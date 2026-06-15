"""

**Cree un programa que muestre el valor más pequeño de una lista sin usar `min()`.**
- Use una variable para comparar uno a uno

"""

def exercise_8():

    my_list = []  # We create the empty list

    query = int(input("How many values do you want to enter in the list?: "))  # We ask the user how many numbers they want to enter in the list

    for i in range(query):  # We create a for loop based on what the user has placed in the query variable
        number = int(input(f"Enter the value number {i+1}: "))  # we ask for the numbers

        my_list.append(number)  # we add the values to the list

    smallest = my_list[0]  # we assign a variable to traverse the list

    for n in my_list:  # we traverse the list with the for loop
        if n < smallest:  # we make the comparison to find the smallest of the numbers
            smallest = n  # we assign it to the variable to show

    print(f"The entered list is: {my_list} and the smallest number is: {smallest}")  # we show the result

exercise_8()
