import functions

is_on = True
print(functions.logo)

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino)")
    if choice == "off":
        is_on = False
    elif choice == "report":
        functions.report()
    elif choice == "espresso":
        check_report = functions.resource_check("espresso")
        if check_report[0]:
            charge = round(functions.process_coin() - functions.MENU["espresso"]["cost"], 2)
            if charge > 0:
                print(f"Your charge: ${charge}")
                functions.make_drink("espresso")
                print("Here is your espresso! Enjoy")
            else:
                print("Sorry, that's not enough money. Money refunded.")
                continue
        else:
            print(check_report[1])
            continue
    elif choice == "latte":
        check_report = functions.resource_check("latte")
        if check_report[0]:
            charge = round(functions.process_coin() - functions.MENU["espresso"]["cost"], 2)
            if charge > 0:
                print(f"Your charge: ${charge}")
                functions.make_drink("latte")
                print("Here is your latte! Enjoy")
            else:
                print("Sorry, that's not enough money. Money refunded.")
                continue
        else:
            print(check_report[1])
            continue
    elif choice == "cappuccino":
        check_report = functions.resource_check("cappuccino")
        if check_report[0]:
            charge = round(functions.process_coin() - functions.MENU["espresso"]["cost"], 2)
            if charge > 0:
                print(f"Your charge: ${charge}")
                functions.make_drink("cappuccino")
                print("Here is your cappuccino! Enjoy")
            else:
                print("Sorry, that's not enough money. Money refunded.")
                continue
        else:
            print(check_report[1])
            continue


