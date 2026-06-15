"""
1. Cree un programa que abra un archivo `.csv` con la información de videojuegos (el que fue generado en el ejercicio 1) y:
- Lea cada línea usando `csv.reader()`
- Muestre el contenido en pantalla de forma legible, línea por línea


"""

import csv

def show_sorted_csv_content(file_path):
    """
    Reads a videogame CSV file and displays its content
    on screen in a readable way, line by line.
    """

    # Open the CSV file in read mode
    with open(file_path, 'r', encoding='utf-8', newline='') as file:

        # Create a CSV reader using comma as delimiter
        reader = csv.reader(
            file,
            delimiter=','
        )

        # Read the first row of the file, which corresponds to the headers
        headers = next(reader)

        # Loop through each data row in the file
        for row in reader:

            # Associate each header with its corresponding value
            # using zip to iterate through both lists in parallel
            for header, value in zip(headers, row):
                print(f"{header}: {value}")

            # Visual separator between videogames
            print("-" * 40)


# Call to the function with the CSV file path
show_sorted_csv_content(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv"
)
