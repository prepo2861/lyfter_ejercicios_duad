"""
3.	Cree un algoritmo que le pregunte al usuario por el sexo de 6 personas, 
    ingresando 1 si es mujer o 2 si es hombre, y muestre al final el porcentaje de mujeres y hombres. 
1.	Ejemplos: 
1.	1, 1, 1, 2, 2, 2 → 50% mujeres y 50% hombres
2.	1, 1, 2, 2, 2, 2 → 33.3% mujeres y 66.6% hombres
3.	1, 1, 1, 1, 1, 2 → 83.3% mujeres y 16.6% hombres

"""

def percentage_women_men():
    try:
        # We create a list to store the values that will be requested later. 
        women = []
        men = []

        for i in range(6):
            gender = int(input(f"Enter the gender of person # {i+1} (1 = woman, 2 = man): "))

            # We validate that the entered data is valid
            if gender < 1 or gender > 2:
                raise ValueError("You must enter 1 or 2")

            # We store in the corresponding list
            if gender == 1:
                women.append(gender)
            else:
                men.append(gender)

        # We calculate quantities and percentages
        total = len(women) + len(men) 
        women_percentage = (len(women) / total) * 100
        men_percentage = (len(men) / total) * 100

        # Final result

        print(f"The number of women is: {len(women)} and their percentage is: {women_percentage:.2f}%")
        print(f"The number of men is: {len(men)} and their percentage is: {men_percentage:.2f}%")

    except ValueError as e:
        print("Error:", e)

percentage_women_men()

