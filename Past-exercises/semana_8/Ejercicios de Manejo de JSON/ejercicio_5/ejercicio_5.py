"""
1. Cree un programa que abra un archivo `.json` con la información de Pokémon ( en base al JSON que fue generado en el ejercicio 1) y:
- Lea el archivo JSON
- Agrupe los Pokémon por tipo (por ejemplo, "agua", "fuego", etc.)
- Calcule y muestre el **promedio de nivel** para cada tipo:

"""

import json


import json

def show_average_level_by_pokemon_type(file_path):
    # Open the JSON file in read mode
    # Load the content as a list of dictionaries
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Dictionary that will be used to group Pokémon by type.
    # Each type will store:
    # - the total sum of levels
    # - the number of Pokémon of that type
    accumulator = {}

    # Iterate through each Pokémon in the list
    for pokemon in data:

        # A Pokémon can have one or more types,
        # so we iterate through the list of types
        for type_ in pokemon["type"]:

            # If the type does not exist yet in the accumulator, initialize it
            if type_ not in accumulator:
                accumulator[type_] = {
                    "total": 0,
                    "count": 0
                }

            # Add the Pokémon's level to the total for the corresponding type
            accumulator[type_]["total"] += pokemon["level"]

            # Increment the count of Pokémon of that type
            accumulator[type_]["count"] += 1

    # Calculate and display the average level for each type
    for type_, info in accumulator.items():

        # The average is obtained by dividing the total levels
        # by the number of Pokémon of the type
        average = info["total"] / info["count"]

        # Display the result with one decimal place
        print(
            f"Type: {type_.capitalize()} → Average level: {average:.1f}"
        )


# Call the function with the JSON file path
show_average_level_by_pokemon_type(
    r"C:\Users\Usuario\Desktop\Ejercicios progra lyfter\Semana_8\Ejercicios de Manejo de JSON\pokemon.json"
)



            

