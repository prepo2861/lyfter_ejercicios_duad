"""
1. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
- Lea el archivo `JSON` de Pokémon
- Recorra la lista de Pokémon y muestre en consola su nombre, tipo y nivel (o cualquier otro atributo definido)

"""

import json

def show_pokemon(file_path):
    """
    Reads a JSON file with Pokémon information and
    displays some of their main attributes on screen.
    """

    # Open the JSON file in read mode
    # Load the entire content as a list of dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Iterate through each Pokémon in the list
        for pokemon in data:

            # Display basic information of the Pokémon
            # Access data using nested keys
            print(
                f"Name: {pokemon['name']['english']} | "
                f"Type: {pokemon['type'][0]} | "
                f"HP: {pokemon['base']['HP']}"
            )


# Call the function with the JSON file path
show_pokemon(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de JSON\pokemon.json"
)