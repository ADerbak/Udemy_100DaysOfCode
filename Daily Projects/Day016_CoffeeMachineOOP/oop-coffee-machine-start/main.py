from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffemachine = CoffeeMaker()
menu = Menu()
register = MoneyMachine()


on = True

while on:
    # TODO: 1. Ask "What would You like (espresso/latte/cappuccino)?"
    user_input = input(f"What would You like ({menu.get_items()})?: ")

    # TODO: 2. Turn off machine using "off"
    if user_input == "off":
        print("Goodbye.")
        on = False
    # TODO: 3. print report using "report"
    elif user_input == "report":
        coffemachine.report()
        register.report()
    # Complete transaction
    else:
        drink = menu.find_drink(user_input)
        if coffemachine.is_resource_sufficient(drink):
            if register.make_payment(drink.cost):
                coffemachine.make_coffee(drink)
        else:
            pass