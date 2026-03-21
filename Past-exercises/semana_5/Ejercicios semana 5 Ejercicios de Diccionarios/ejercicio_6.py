"""
Dada una lista de productos vendidos, donde cada uno tiene categoría y precio, cree un diccionario que acumule el total por categoría.
"""


def exercise_6():

    products = [
        {"name": "Monitor", "category": "Electrónica", "price": 200},
        {"name": "Teclado", "category": "Electrónica", "price": 50},
        {"name": "Silla", "category": "Muebles", "price": 120},
        {"name": "Mesa", "category": "Muebles", "price": 180},
        {"name": "Mouse", "category": "Electrónica", "price": 25},
    ]

    result = {}

    for item in products:  # loops through each product (dictionary)
        category = item["category"]  # gets the category.
        price = item["price"]  # gets the price

        result[category] = result.get(category, 0) + price  # gets the current total or 0 if it doesn't exist and then adds the price
        
    print(result)  # Shows the result

exercise_6()
