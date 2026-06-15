"""
2. Cree un programa que permita agregar un Pokémon nuevo al archivo de la lección de JSON.
    1. Debe leer el archivo para importar los Pokémones existentes.
    2. Luego debe pedir la información del Pokémon a agregar.
    3. Finalmente debe guardar el nuevo Pokémon en el archivo.
"""
import json

def add_pokemon_to_json(file_path):
    # Open the JSON file in read mode
    # Load the entire content as a list of dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)  # List of existing Pokémon

    # Create the dictionary that will represent the new Pokémon
    new_pokemon = {
        "name": {
            "english": input("Enter the Pokémon's name: ")
        },
        "level": int(input("Enter the Pokémon's level: ")),
        "type": [
            input("Enter the Pokémon's type: ")
        ],
        "base": {}
    }

    # Prompt the user for the Pokémon's base stats
    # and store them within the "base" dictionary
    for stat in ["HP", "Attack", "Defense", "Sp. Attack", "Sp. Defense", "Speed"]:
        new_pokemon["base"][stat] = int(
            input(f"Enter the value for {stat}: ")
        )

    # Add the new Pokémon to the existing list
    data.append(new_pokemon)

    # Open the JSON file in write mode to save the changes
    # Use indentation to make the file readable
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

    # Confirmation message
    print(
        f"The Pokémon {new_pokemon['name']['english']} has been added successfully."
    )

# Call the function with the JSON file path
add_pokemon_to_json(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de JSON\pokemon.json"
)