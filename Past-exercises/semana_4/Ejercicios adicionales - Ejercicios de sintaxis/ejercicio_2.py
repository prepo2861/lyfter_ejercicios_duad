"""
2.Cree un pseudocódigo que le pida un tiempo en segundos al usuario y calcule si es menor o mayor a 10 minutos. 
  Si es menor, muestre cuantos segundos faltarían para llegar a 10 minutos. 
  Si es mayor, muestre “Mayor”. Si es exactamente igual, muestre “Igual”. 
"""

def remaining_time():
    try:
        # We start with user validations so that only numbers greater than 0 can be entered
        time = 600
        user_time = int(input("Enter the time in seconds you want to be calculated:  "))

        if user_time <= 0: 
            raise ValueError("Error, you can only enter numbers greater than 0")
        
        # We start defining the conditionals to determine the practice result

        if user_time < time:
            result = time - user_time
            print(f"The entered time is {user_time} seconds, so what is missing to reach 10 minutes is: {result} seconds")
        elif user_time > time:
            print("The entered time is greater")
        else:
            print("The entered time is equal")
        
    except ValueError:
        print("Error, you can only enter numbers greater than 0")

remaining_time()
