"""
1. Cree un programa que:
- Pida al usuario una línea de texto
- Agregue esa línea **al final** de un archivo existente
- Si el archivo no existe, lo crea automáticamente


"""


from pathlib import Path

# Creates the file "file.txt" in the current directory if it doesn't exist
# (does not overwrite the file if it already exists)
Path("file.txt").touch(exist_ok=True)


def add_line(path):
    """
    Prompts the user for a line of text and adds it
    to the end of a text file.
    """

    # Opens the file in 'append' mode to add content at the end
    with open(path, 'a', encoding='utf-8') as file:

        # Prompts the user for the text they want to add
        new_text = input("Enter the text you want to add to the file: ")

        # Writes the text to the file and adds a line break
        file.write(new_text + "\n")

        # Confirmation message
        print("Text added successfully!!")


# Call to the function with the full path of the file
add_line(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_5\file.txt"
)