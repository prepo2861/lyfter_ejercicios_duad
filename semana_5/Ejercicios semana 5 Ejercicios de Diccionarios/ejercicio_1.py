"""
1. Cree un diccionario que guarde la siguiente información sobre un hotel:
    - `nombre`
    - `numero_de_estrellas`
    - `habitaciones`
- El value del key de `habitaciones` debe ser una lista, y cada habitación debe tener la siguiente información:
    - `numero`
    - `piso`
    - `precio_por_noche`

"""

def exercise_1():  # We create the function

    hotel_information = {"Name": "Gran Hotel Costa Rica, Curio Collection by Hilton", 
                         "Number of stars": 4,
                         "Rooms": [{"number": 101,
                                    "floor": 1,
                                    "price_per_night": 107000},
                                   {"number": 102,
                                    "floor": 1,
                                    "price_per_night": 115000},
                                   {"number": 103,
                                    "floor": 2,
                                    "price_per_night": 124000}                  
                            ]
                         }   # We create the dictionary with the requested information

exercise_1()
