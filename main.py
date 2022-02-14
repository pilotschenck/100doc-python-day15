MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def checkResources(drinkSelection):
    for ingredient in MENU.get(drinkSelection).get("ingredients"):
        print(MENU.get(drinkSelection).get("ingredients").get(ingredient))
        if int(MENU.get(drinkSelection).get("ingredients").get(ingredient)) > int(resources.get(ingredient)):
            print("Sorry, there is not enough " + str(ingredient))
            return False
        else:
            print("There is enough " + str(ingredient) + ".")

    return True

def verifyPayment():
    insertedQuarters = input("How many quarters will you insert?")
    insertedDimes    = input("How many dimes will you insert?")
    insertedNickles  = input("How many nickles will you insert?")
    insertedPennies  = input("How many pennies will you insert?")
    insertedCoins = {"quarters" : insertedQuarters, "dimes" : insertedDimes, "nickles" : insertedNickles, "pennies":
        insertedPennies}

    try:
        int(insertedQuarters)
        int(insertedDimes)
        int(insertedNickles)
        int(insertedPennies)
        isValid = True
    except ValueError:
        print("Invalid entry: enter an integer value for coinage.")
        isValid = False
        insertedCoins = {}

    return isValid, insertedCoins

def processPayment(drinkSelection, coinPayment):
    totalsum = 0.00

    for coins in coinPayment:
        if coins == "quarters":
            totalsum = totalsum + (0.25 * coins)
        elif coins == "dimes":
            totalsum = totalsum + (0.10 * coins)
        elif coins == "nickles":
            totalsum = totalsum + (0.05 * coins)
        elif coins == "pennies":
            totalsum = totalsum + (0.01 * coins)

    if totalsum >= MENU.get(drinkSelection).get("cost"):
        change = totalsum - MENU.get(drinkSelection).get("cost")

    else:
        print("Sorry, that's not enough money. Money refunded.")
        change = totalsum

    return change



selection = input("What would you like? (espresso/latte/cappuccino): ")
print("Your selection is: " + selection)

if selection.lower() == "off":
    quit()
elif selection.lower() == "report":
    for x in resources:
        print(str(x) + ": " + str(resources.get(x)))
elif selection.lower() != "espresso" or "latte" or "cappuccino":
    print("Not a valid menu selection, please enter a valid drink.")

test = checkResources(selection)
if test == True:
    verifyPayment()

