import math
pizzaSize = float(1)
pizzaCost = float(1)
pizzaList = []

def pizzaValuator():
    anotherPizza = "Y"
    while anotherPizza == "Y" :
        pizzaStore = input("Where is this pizza from? ")
        pizzaSize = float(input("How big (in inches) is the pizza? "))
        pizzaCost = float(input("How much does it cost? "))
        pizzaValue = round(pizzaCost / (math.pi * (pizzaSize / 2) ** 2),3)
        print(pizzaValue)
        pizzaList.append(pizzaStore + " " + str(pizzaSize))
        pizzaList.append(pizzaValue)
        anotherPizza = input("Would you like to enter another pizza? (Y/N) ")
    print ("Thank you!" )
    print (pizzaList)

pizzaValuator()

