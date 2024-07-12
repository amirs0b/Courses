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
    },
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0


def make_coffee(order):
    for ingredient in MENU[order]["ingredients"]:
        resources[ingredient] -= MENU[order]["ingredients"][ingredient]
    print(f"Here is your {order} ☕. Enjoy!")


def is_resource_sufficient(order_ingredients):
    """
    Checks if there are sufficient resources to fulfill the given order based on the available resources.
    
    :param order_ingredients: A dictionary containing the required ingredients for the order.
    :return: True if there are enough resources, False otherwise.
    """
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """
    A function that processes the coins inserted by the user and calculates the total amount based on the number of quarters, dimes, nickels, and pennies entered.
    Returns the total amount of money inserted.
    """
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def check_transaction_successful(money_received, drink_cost):
    """
    A function that checks if the money received is enough to cover the cost of the drink. 
    It calculates the change if the money is sufficient and updates the global money variable.
    
    :param money_received: The amount of money received from the user.
    :param drink_cost: The cost of the drink the user wants to purchase.
    :return: True if the transaction is successful, False if the money is not enough.
    """
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global money
        money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


machine_on = True

while machine_on:
    order = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${money}")
    elif order == "off":
        machine_on = False
    elif order in MENU:
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if check_transaction_successful(payment, drink["cost"]):
                make_coffee(order)
    else:
        print("Sorry wrong order. Please try again.")
        re_Run = input("Would you like to try again? (y/n): ")
        if re_Run == "y":
             machine_on = True
        else:
            print("Thank you!")
            machine_on = False