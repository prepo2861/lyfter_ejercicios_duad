"""
Cree una clase base Vehicle con los atributos:

_brand
_year

Agregue un método get_info() que devuelva una descripción del vehículo.
Luego cree dos clases hijas:

Car
Motorcycle

Cada una debe agregar su propio atributo (por ejemplo, doors o type) y 
sobrescribir el método get_info() para incluir esta información adicional.


"""


class Vehicle:

    # Constructor used to initialize the vehicle information
    def __init__(self, brand, year):

        # Validate that the brand is not empty
        if not brand.strip():
            raise ValueError(
                "Brand cannot be empty."
            )

        self._brand = brand

        # Validate that the year is positive
        if year <= 0:
            raise ValueError(
                "Year must be positive."
            )

        self._year = year

    # Return the vehicle brand
    @property
    def brand(self):
        return self._brand

    # Return the vehicle year
    @property
    def year(self):
        return self._year

    # Return the basic vehicle information
    def get_info(self):

        return (
            f"Brand: {self.brand} || "
            f"Year: {self.year}"
        )


class Car(Vehicle):

    # Constructor used to initialize a Car object
    def __init__(self, brand, year, doors):

        # Initialize the inherited attributes
        super().__init__(brand, year)

        # Validate that the number of doors is positive
        if doors <= 0:
            raise ValueError(
                "Doors must be positive."
            )

        self.doors = doors

    # Override the parent method to include the number of doors
    def get_info(self):

        # Get the information from the parent class
        info = super().get_info()

        # Return the complete car information
        return f"{info} || Doors: {self.doors}"


class Motorcycle(Vehicle):

    # Constructor used to initialize a Motorcycle object
    def __init__(self, brand, year, bike_type):

        # Initialize the inherited attributes
        super().__init__(brand, year)

        # Validate that the motorcycle type is not empty
        if not bike_type.strip():
            raise ValueError(
                "Bike type cannot be empty."
            )

        self.bike_type = bike_type

    # Override the parent method to include the motorcycle type
    def get_info(self):

        # Get the information from the parent class
        info = super().get_info()

        # Return the complete motorcycle information
        return f"{info} || Type: {self.bike_type}"
       
