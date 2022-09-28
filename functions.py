logo = '''
              _..,----,.._
            .-;'-.,____,.-';
           (( |            |
            `))            ;
             ` \          /
            .-' `,.____.,' '-.
           (     '------'     )
            `-=..________..--'
        '''

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0.00
}


def report():
    """Prints current resources"""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${resources['money']}")


def resource_check(drink):
    prompt = ""
    check_report = [True, ""]
    if MENU[drink]["ingredients"]["water"] > resources["water"]:
        check_report[0] = False
        prompt += "There is not enough water. "
    if MENU[drink]["ingredients"]["milk"] > resources["milk"]:
        check_report[0] = False
        prompt += "There is not enough milk. "
    if MENU[drink]["ingredients"]["coffee"] > resources["coffee"]:
        check_report[0] = False
        prompt += "There is not enough coffee. "
    check_report[1] = prompt
    return check_report


def process_coin():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    return (quarters * 0.25) + (dimes * 0.1) + (nickles * 0.05) + (pennies * 0.01)


def make_drink(drink):
    resources["money"] += MENU[drink]["cost"]
    resources["water"] -= MENU[drink]["ingredients"]["water"]
    resources["milk"] -= MENU[drink]["ingredients"]["milk"]
    resources["coffee"] -= MENU[drink]["ingredients"]["coffee"]