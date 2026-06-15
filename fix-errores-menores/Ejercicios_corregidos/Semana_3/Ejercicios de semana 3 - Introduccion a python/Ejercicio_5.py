"""
Cree un algoritmo que defina una cantidad de metros (por ejemplo, 5) y luego use print() para mostrar cuántos centímetros son
Ejemplo:
Salida:
"5 metros son 500 centímetros"

"""

import sys

def Conversion():
    try:
        try:  # Request and validate meters
            meters = int(input("Enter the number of meters to convert: "))
            
            if meters < 0:
                raise ValueError("You must enter only positive numeric values")
            
        except ValueError:
            raise ValueError("You must enter only positive numeric values")
        
        centimeters = meters * 100 # Perform the conversion formula

        # Display the result
        print("*****************************************************************************************")
        print(f"{meters} meters is {centimeters} cm")
        print("*****************************************************************************************")

    except ValueError as e:
        print("Error!", e)

Conversion()
