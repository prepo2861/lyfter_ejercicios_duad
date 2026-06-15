"""
Lea sobre el resto de métodos del módulo csv [aqui ](https://docs.python.org/es/3/library/csv.html)
y cree una version alternativa del ejercicio de arriba que guarde el archivo separado por tabulaciones en vez de por comas.
"""

import csv

def tabular_csv(input_path, output_path):
    """
    Reads a CSV file separated by commas and generates
    an alternative version of the same file separated
    by tabs (TSV format).
    """

    # Open the original CSV file in read mode.
    # csv.reader is used because we need to read each line of the file.
    with open(input_path, 'r', encoding='utf-8', newline='') as file:
        reader = csv.reader(
            file,
            delimiter=','   # Delimiter of the original CSV
        )

        # Convert the content of the reader into a list
        # to be able to reuse the data when writing the new file
        rows = list(reader)

    # Open the output file in write mode.
    # This file will contain the alternative version separated by tabs.
    with open(output_path, 'w', encoding='utf-8', newline='') as new_file:
        writer = csv.writer(
            new_file,
            delimiter='\t'  # Tab delimiter (TSV)
        )

        # Write all the read rows to the new file
        writer.writerows(rows)

    # Confirmation message upon finishing the process
    print("Alternative version of the file created successfully (TSV)")


# Call to the function indicating:
# - Path of the original CSV file
# - Path of the alternative file in TSV format
tabular_csv(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames.csv",
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de CSVs\videogames_tsv.csv"
)