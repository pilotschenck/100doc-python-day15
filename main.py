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
    "money": 0.0,
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
    insertedQuarters = input("How many quarters will you insert? ")
    insertedDimes = input("How many dimes will you insert? ")
    insertedNickles = input("How many nickles will you insert? ")
    insertedPennies = input("How many pennies will you insert? ")
    insertedCoins = {"quarters": insertedQuarters, "dimes": insertedDimes, "nickles": insertedNickles, "pennies":
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
            totalsum = totalsum + (0.25 * float(coinPayment[coins]))
        elif coins == "dimes":
            totalsum = totalsum + (0.10 * float(coinPayment[coins]))
        elif coins == "nickles":
            totalsum = totalsum + (0.05 * float(coinPayment[coins]))
        elif coins == "pennies":
            totalsum = totalsum + (0.01 * float(coinPayment[coins]))

    if totalsum >= MENU.get(drinkSelection).get("cost"):
        change = totalsum - MENU.get(drinkSelection).get("cost")

    else:
        print("Sorry, that's not enough money. Money refunded.")
        change = totalsum
        return False

    return change


def selectionLoop():
    selection = input("What would you like? (espresso/latte/cappuccino): ")
    print("Your selection is: " + selection)

    if selection.lower() == "off":
        quit()
    elif selection.lower() == "report":
        for x in resources:
            if str(x) in ["water", "milk"]:
                print(str(x).title() + ": " + str(resources.get(x)) + "ml")
            if str(x) in ["coffee"]:
                print(str(x).title() + ": " + str(resources.get(x)) + "g")
            if str(x) in ["money"]:
                print(str(x).title() + ": " + "$" + str(resources.get(x)))

    elif selection.lower() not in ["espresso", "latte", "cappuccino"]:
        print("Not a valid menu selection, please enter a valid drink.")
    else:
        if checkResources(selection) == True:
            validMoney, coinage = verifyPayment()
            if validMoney == True:
                change = processPayment(selection, coinage)
                if change != False:
                    if change > 0:
                        print("Here is $" + str(round(change, 2)) + " in change.")
                    for ingredient in MENU.get(selection).get("ingredients"):
                        resources[ingredient] = int(resources.get(ingredient)) - \
                                                         int(MENU.get(selection).get("ingredients").get(ingredient))
                    resources["money"] = resources["money"] + MENU.get(selection).get("cost")
                    print("Here is your " + selection + ". Enjoy!")

while True:
    selectionLoop()