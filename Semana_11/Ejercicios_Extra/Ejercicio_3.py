"""
Cree una clase Product con:
Nombre, precio y cantidad
Cree una clase Inventory que:
Guarde productos en una lista
Tenga métodos para:
Agregar un producto
Mostrar todos los productos
Calcular el valor total del inventario

"""

class Product:

    # Constructor used to initialize a Product object
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:

    # Constructor that initializes an empty list of products
    def __init__(self):
        self.products = []

    # Adds one or more products to the inventory
    def add_product(self):

        while True:

            try:
                product_name = input("Please enter the name of the product: ")

                # Validate product name
                if (
                    not product_name.strip()
                    or any(char.isdigit() for char in product_name)
                    or any(char in '+-*/=!@#$%^&()[];:{}",.<>?' for char in product_name)
                ):
                    raise ValueError("Invalid product name.")

                product_price = float(
                    input(f"Please enter the price of {product_name}: ")
                )

                # Validate product price
                if product_price <= 0:
                    raise ValueError("Price must be greater than 0.")

                product_quantity = int(
                    input(f"Please enter the quantity of {product_name}: ")
                )

                # Validate product quantity
                if product_quantity <= 0:
                    raise ValueError("Quantity must be greater than 0.")

                # Create a Product object
                new_product = Product(
                    product_name,
                    product_price,
                    product_quantity
                )

                # Add the product to the inventory list
                self.products.append(new_product)

                print(f"The product {product_name} has been added!")

                menu = input(
                    "Would you like to enter another product? (Y/N): "
                ).lower()

                if menu == "n":
                    return

            except ValueError as e:
                print(f"Error: {e}")

    # Displays all products stored in the inventory
    def show_products(self):

        if not self.products:
            print("No products registered!")
            return

        for i, product in enumerate(self.products, start=1):
            print("-" * 40)
            print(f"Product #{i}")
            print(f"Product name: {product.name}")
            print(f"Product price: ${product.price:.2f}")
            print(f"Product quantity: {product.quantity}")

        input("\nPress Enter to continue...")

    # Calculates and displays the total value of the inventory
    def get_total_value(self):

        if not self.products:
            print("No products registered!")
            return

        total = 0

        for product in self.products:
            total += product.price * product.quantity

        print(f"Total inventory value: ${total:.2f}")


inventory = Inventory()

inventory.add_product()
inventory.show_products()
inventory.get_total_value()