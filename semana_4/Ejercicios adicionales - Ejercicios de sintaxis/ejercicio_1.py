""""
1.	Cree un pseudocódigo que le pida un precio de producto al usuario, calcule su descuento y muestre el precio final tomando en cuenta que: 
.	Si el precio es menor a 100, el descuento es del 2%.
.	Si el precio es mayor o igual a 100, el descuento es del 10%.
.	Ejemplos: 
.	120 → 108
.	40 → 39.2

"""


def discount():
    try:
        # We start with user validations so that only numbers can be entered

        price = int(input("Please enter the price to calculate: "))  # We validate so that only numbers greater than 1 can be entered
        if price < 1: 
            raise ValueError("Error, you can only enter numbers greater than 1")
        
        if price < 100:  # We implement the conditional as requested in the practice and placed in the pseudocode and flowchart
            new_discount = price * 0.2
        elif price >= 100:
            new_discount = price * 0.1
        
        new_price = price - new_discount

        # Final result

        print(f"The entered price is: {price}, so your discount is {new_discount} and your final price will be: {new_price} ")

    except ValueError:
        print("Error, you can only enter numbers greater than 1")
    

discount()
