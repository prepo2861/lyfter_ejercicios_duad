"""
1. Cree un programa que me permita ingresar información de `n` cantidad de videojuegos y los guarde en un archivo `csv`.
    1. Debe incluir:
        1. Nombre
        2. Género
        3. Desarrollador
        4. Clasificación ESRB

"""



import csv
import os

# Tuple that defines the headers of the CSV file.
# These will be the column names.
videogame_headers = (
    'Name',
    'Genre',
    'Developer',
    'ESRB Rating'
)

def create_csv(file_path):
    """
    Allows entering information for multiple videogames
    and saving it in a CSV file.
    """

    # Checks if the file already exists to avoid duplicating headers
    file_exists = os.path.isfile(file_path)

    # Opens the file in 'append' mode to add new data without deleting existing ones
    # Always works with comma delimiter to maintain standard CSV format
    with open(file_path, 'a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(
            file,
            fieldnames=videogame_headers,
            delimiter=','   # Comma delimiter
        )

        # If the file does not exist, headers are written only once
        if not file_exists:
            writer.writeheader()

        # Loop to allow entering multiple videogames
        while True:
            videogame_data = {}

            # Prompts the user for each data defined in the headers
            for header in videogame_headers:
                videogame_data[header] = input(f"Enter the {header}: ")

            # Writes a row in the CSV file with the entered data
            writer.writerow(videogame_data)

            # Asks if they want to continue entering more data
            continue_input = input("Do you want to enter another data? (y/n): ").lower()
            if continue_input != 'y':
                break

    # Confirmation message upon finishing the process
    print("Data added successfully!")


# Call to the function with the CSV file path
create_csv(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv"
)


