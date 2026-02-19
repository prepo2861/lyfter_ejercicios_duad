"""
1. Cree un programa que lea nombres de canciones de un archivo (línea por línea) y guarde en otro archivo los mismos nombres ordenados alfabéticamente.

"""

def read_song_list(path_read):
    """
    Reads a text file line by line and displays its content in the console.
    Does not modify the file or return data.
    """
    with open(path_read, encoding='utf-8') as file:
        for line in file.readlines():
            print(line.strip())  # .strip() removes line breaks and extra spaces


def sort_song_list(path_sorted, path):
    """
    Reads the original file (path), sorts its content alphabetically,
    and writes the result to a new file (path_sorted).
    Also prints the sorted content to the screen.
    """
    
    # Open the original file and read all lines without line breaks
    with open(path, encoding='utf-8') as file:
        lines = file.read().splitlines()

    # Sort the list of songs alphabetically
    sorted_lines = sorted(lines)

    # Write the sorted result to a new file (or overwrite if it already exists)
    with open(path_sorted, 'w', encoding='utf-8') as file:
        for line in sorted_lines:
            file.write(line + "\n")  # Save line by line
            print(line)  # Display the already sorted content in the console


def main():
    """
    Main function:
    1. Displays the content of the original file
    2. Generates a new file with the content sorted alphabetically
    """

    # Path of the original file
    read_song_list(
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_1\songs_list.txt"
    )

    print("************************************************************************************************")

    # Path of the file where the sorted version will be saved
    sort_song_list(
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_1\songs_list_sorted.txt",
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_1\songs_list.txt"
    )


main()

