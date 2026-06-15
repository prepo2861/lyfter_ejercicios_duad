"""
1. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
- Lea el archivo JSON de Pokémon
- Para cada Pokémon, muestre sus **estadísticas principales** (por ejemplo: `ataque`, `defensa`, `velocidad`, etc.)

"""


import json

def show_pokemon_stats(file_path):
    # Open the JSON file in read mode
    # Load the entire content as a list of dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

        # Iterate through each Pokémon in the file
        for pokemon in data:

            # Display the Pokémon's base stats
            # Each stat is obtained from the nested "base" dictionary
            print(
                f"Name: {pokemon['name']['english']}  \n"
                f"HP: {pokemon['base']['HP']}  \n"
                f"Attack: {pokemon['base']['Attack']} \n"
                f"Defense: {pokemon['base']['Defense']} \n"
                f"Sp Attack: {pokemon['base']['Sp. Attack']}  \n"
                f"Sp Defense: {pokemon['base']['Sp. Defense']}   \n"
                f"Speed: {pokemon['base']['Speed']}  \n"
                f"****************************************\n"
            )


# Call the function with the JSON file path
show_pokemon_stats(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de JSON\pokemon.json"
)