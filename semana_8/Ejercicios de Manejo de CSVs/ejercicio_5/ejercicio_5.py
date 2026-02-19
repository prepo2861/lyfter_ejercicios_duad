"""
1. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Cuente cuántos videojuegos hay de **cada género**
- Muestre el resultado de forma ordenada

"""


import csv
from collections import Counter

def show_game_count_by_category(file_path):
    """
    Reads a videogame CSV file and displays the count
    of videogames grouped by ESRB rating.
    """

    # Create a counter to store the number of videogames
    # for each ESRB rating
    counter = Counter()

    # Open the CSV file in read mode
    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        # Create a dictionary reader to access fields by name
        reader = csv.DictReader(
            file,
            delimiter=','
        )

        # Loop through each row in the file
        for row in reader:

            # Increment the counter for the corresponding ESRB rating
            # strip() is used to avoid errors due to whitespace
            counter[row["ESRB Rating"].strip()] += 1

        # Display the results sorted alphabetically by rating
        for rating in sorted(counter):
            print(f"{rating}: {counter[rating]}")


# Call to the function with the CSV file path
show_game_count_by_category(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv"
)

        