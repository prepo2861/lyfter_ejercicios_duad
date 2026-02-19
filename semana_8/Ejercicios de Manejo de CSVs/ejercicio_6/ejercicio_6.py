"""
1. Cree un programa que abra un archivo `.csv` con la información de videojuegos( en base al CSV que fue generado en el ejercicio 1) y:
- Lea el archivo `.csv` con videojuegos
- Pida al usuario ingresar el nombre de un **desarrollador** (ej. `"Ubisoft"`)
- Muestre todos los videojuegos desarrollados por esa empresa en formato legible:
"""

import csv

def show_games_by_developer(file_path):
 

    # Open the CSV file in read mode
    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        # Create a dictionary reader to access data by header
        reader = csv.DictReader(
            file,
            delimiter=','  # The CSV file is separated by commas
        )

        # Prompt the user for the developer name to search
        # Normalize the input to avoid case sensitivity issues
        filter_developer = input(
            "Enter the name of a videogame developer: "
        ).strip().lower()

        # Flag to check if at least one videogame was found
        found = False

        # Informative header for the screen output
        print(f"\nVideogames developed by {filter_developer}:\n")

        # Loop through each row in the CSV file
        for row in reader:

            # Compare the videogame's developer with the entered filter
            if row["Developer"].strip().lower() == filter_developer:
                found = True

                # Visual separator before displaying the videogame data
                print("-" * 40)

                # Display all fields of the found videogame
                for header in reader.fieldnames:
                    print(f"{header}: {row[header]}")

                # Visual separator after displaying the data
                print("-" * 40)

        # Message if no videogame is found
        if not found:
            print("Developer not found in the list")


# Call to the function with the CSV file path
show_games_by_developer(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv"
)