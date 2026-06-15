"""
1. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y::
- Lea el archivo `JSON` de Pokémon
- Pida al usuario un tipo de Pokémon
- Muestre todos los Pokémon que sean de ese tipo

"""

import json

def show_pokemon_by_type(file_path):
    """
    Reads a JSON file with Pokémon information and displays
    all Pokémon that match a type entered by the user.
    """

    # Open the JSON file in read mode
    # Load the entire content as a list of dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Prompt the user for the type of Pokémon to search
    # Normalize the input to avoid errors due to case sensitivity
    requested_type = input(
        "Enter the type of Pokémon you want to search (water, electric, fire, etc.): "
    ).strip().lower()

    # Flag to check if at least one Pokémon was found
    found = False

    # Informative header for the output
    print(f"\nPokémon of type {requested_type}:")

    # Iterate through each Pokémon in the file
    for pokemon in data:

        # A Pokémon can have one or more types,
        # so we iterate through the list of types
        for type_ in pokemon["type"]:

            # Compare the Pokémon's type with the entered filter
            if type_.strip().lower() == requested_type:
                print(f"- {pokemon['name']['english']}")
                found = True

    # Message in case no matches are found
    if not found:
        print("No Pokémon of that type were found in the saved data.")


# Call the function with the JSON file path
show_pokemon_by_type(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de JSON\pokemon.json"
)