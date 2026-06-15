"""
Cree un programa que lea un archivo con texto línea por línea, quite los saltos de línea (\n) y escriba todo el contenido en un solo renglón en un nuevo archivo

"""

def show_file(path_read):
    """
    Reads a text file and displays its content line by line,
    removing the line breaks at the end of each one.
    """

    # Open the file in read mode with UTF-8 encoding
    with open(path_read, encoding='utf-8') as file:
        
        # Loop through each line in the file
        for line in file.readlines():
            
            # Print the line without extra spaces or line breaks
            print(line.strip())


def remove_line_breaks(path, path_sorted):
    """
    Reads a text file, removes the line breaks,
    and saves all the content in a single line in a new file.
    """

    # Open the original file in read mode
    with open(path, encoding='utf-8') as file:
        
        # Read the entire file and split the lines into a list
        lines = file.read().splitlines()

    # Remove unnecessary spaces at the beginning and end of each line
    cleaned_lines = [line.strip() for line in lines]

    # Open (or create) the destination file in write mode
    with open(path_sorted, 'w', encoding='utf-8') as file:
        
        # Join all lines into a single one separated by spaces
        file.write(" ".join(cleaned_lines))

        # Confirmation message for the user
        print("The file has been processed. You can check the txt!")



        
    
    

def main():
    show_file(r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_2\test.txt")

    remove_line_breaks(r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_2\test.txt" , r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de Archivos\ejercicio_2\solution.txt")

main()
