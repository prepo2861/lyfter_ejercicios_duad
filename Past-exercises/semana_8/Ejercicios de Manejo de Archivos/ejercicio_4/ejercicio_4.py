"""
1. Cree un programa que:
- Lea un archivo línea por línea
- Convierta cada línea a **mayúsculas**
- Escriba el contenido en un **nuevo archivo**


"""

def read_file(path):
    """
    Displays the original content of a text file on the screen.
    """

    # Informative message for the user
    print("Original file")
    print("*****************************************")

    # Opens the file in read mode with UTF-8 encoding
    with open(path, encoding='utf-8') as file:
        
        # Loops through each line in the file
        for line in file.readlines():
            
            # Prints the line removing line breaks and extra spaces
            print(line.strip())


def upper_file(path, upper_path):
    """
    Reads a text file and saves its content in uppercase
    in a new file.
    """

    # Opens the original file in read mode
    with open(path, encoding='utf-8') as file:
        
        # Reads all the content and stores it in a list of lines
        lines = file.read().splitlines()

    # Opens (or creates) the destination file in write mode
    with open(upper_path, 'w', encoding='utf-8') as file:
        
        # Loops through each line and writes it in uppercase
        for line in lines:
            file.write(line.upper() + "\n")

        # Confirmation messages
        print("*****************************************")
        print("File updated. You can check the txt")
        print("*****************************************")


def main():
    """
    Main function that executes the program flow.
    """

    # Displays the original content of the file
    read_file(
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_4\file.txt"
    )

    # Creates a new file with the content in uppercase
    upper_file(
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_4\file.txt",
        r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_4\new_file.txt"
    )


# Program entry point
main()
