"""
Cree un programa que reciba una lista de números y calcule el promedio de los valores, luego cree una nueva lista con solo los valores mayores al promedio

"""


def exercise_9():

    my_list = []  # We create the empty list

    query = int(input("How many values do you want to enter in the list?: "))  # We ask the user how many numbers they want to enter in the list

    for i in range(query):  # We create a for loop based on what the user has placed in the query variable
        number = int(input(f"Enter the value number {i+1}: "))  # we ask for the numbers

        my_list.append(number)  # we add the values to the list

    sum = 0  # we create the sum variable to add up each value in the list
    counter = 0  # counter will add up the content in the list (like a len)

    for n in my_list:  # we create the for loop that will traverse the list
        sum += n
        counter += 1

    average = sum / counter  # we create the average variable

    new_list = []  # we create a new list where it will store the values that are greater than the average

    for j in my_list:  # we do the traversal again
        if j > average:  # we make the comparison to find the values greater than the average
            new_list.append(j)  # we save them in the new list

    print(f"The entered list was: {my_list}, the average obtained is: {average} and the values greater than the average were: {new_list}")  # we show the result

exercise_9()
