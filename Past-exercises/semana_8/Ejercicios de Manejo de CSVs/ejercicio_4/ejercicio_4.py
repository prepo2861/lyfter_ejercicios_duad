"""
1. Cree un programa que abra un archivo `.csv` con la información de videojuegos ( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo CSV de videojuegos
- Pida al usuario una clasificación ESRB (por ejemplo: "T")
- Muestre todos los videojuegos que tengan esa clasificación

"""

import csv

def show_videogame_by_rating(file_path):
    """
    Reads a videogame CSV file and displays on screen
    all videogames that match an ESRB rating
    entered by the user.
    """

    # Open the CSV file in read mode
    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        # Create a dictionary reader to access data by header
        reader = csv.DictReader(
            file,
            delimiter=','  # The CSV file is separated by commas
        )

        # Prompt the user for the ESRB rating to filter
        # Normalize the input to avoid errors due to case sensitivity
        filter_rating = input(
            "Enter an ESRB rating (E, E10+, T, M, AO): "
        ).strip().upper()

        # Flag to check if at least one videogame was found
        found = False

        # Loop through each row in the CSV file
        for row in reader:

            # Compare the videogame's ESRB rating with the entered filter
            if row["ESRB Rating"].strip().upper() == filter_rating:
                print(row["Name"])
                found = True

        # If no videogame was found with the specified rating
        if not found:
            print("No videogame found with that rating")


# Call to the function with the CSV file path
show_videogame_by_rating(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv"
)
                



