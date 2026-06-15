"""
1. Cree un programa que abra un archivo de texto y cuente cuántas palabras contiene en total.

(Considere que las palabras están separadas por espacios y/o saltos de línea)

"""

def word_counter(path):
    """
    Counts the total number of words contained in a text file.
    """

    # Variable to store the total number of words
    total = 0

    # Opens the file in read mode with UTF-8 encoding
    with open(path, encoding='utf-8') as file:

        # Iterates through the file line by line
        for line in file:
            
            # Splits the line into words and adds their count to the total
            total += len(line.split())
    
    # Displays the final result
    print(f"This file contains {total} words")


# Call to the function with the file path
word_counter(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_3\file.txt"
)