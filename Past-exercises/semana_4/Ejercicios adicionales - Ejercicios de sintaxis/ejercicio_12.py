"""
3. **Convertidor de unidades de temperatura**
    - Pida al usuario ingresar una temperatura en Celsius
    - Conviértala a Fahrenheit y Kelvin
    - Muestre los tres valores
"""

def converter():
    # We create validations so that only numbers are entered
    try:
        celsius = float(input("Enter the temperature in Celsius to convert to Fahrenheit and Kelvin: "))

        kelvin = celsius + 273.15  # We use the formula to convert from Celsius to Kelvin
        fahrenheit = (celsius * 9 / 5) + 32  # We use the formula to convert from Celsius to Fahrenheit

        print(f"The conversion of {celsius}°C is: {kelvin:.2f}K and {fahrenheit:.2f}°F")  # Result with .2f to show only 2 decimals

    except ValueError:
        print("Error, only numeric values can be entered")

converter()
