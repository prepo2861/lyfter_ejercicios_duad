"""
2.	Cree un algoritmo que le pida al usuario una velocidad en km/h y la convierta a m/s. 
Recuerda que 1 km == 1000m y 1 hora == 60 minutos * 60 segundos. 
1.	Ejemplos: 
1.	73 → 20.27
2.	50 → 13.88
3.	120 → 33.33

"""

def convert():
    # We validate that the user only enters numeric values
    try:
        kilometers = float(input("Please enter the kilometers per hour to convert to meters per second: "))
        if kilometers <= 0:  # We validate so that only values greater than 0 are entered
            raise ValueError
        
        meters_per_second = kilometers * 1000 / 3600  # direct formula
        print(f"The conversion of {kilometers} km/h to m/s is: {meters_per_second:.2f}")  # We ask the f-string to show only 2 decimals of the result
    except ValueError:
        print("Error, you can only enter positive numeric values")

convert()

