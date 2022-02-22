
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

on = True
paid_check = True
resources_check = True
ordering_check = True
money = 0.00

# TODO: 4. Check if resources are sufficient
def check_resources(input):
    global resources
    global resources_check
    item = MENU[input]
    if item in ['latte', 'cappuccino']:
        if ((item['ingredients']['water'] > resources['water'])
                or (item['ingredients']['milk'] > resources['milk'])
                or (item['ingredients']['coffee'] > resources['coffee'])):
            print("insufficient resources")
            resources_check = False
            return resources_check
    else:
        if item['ingredients']['water'] > resources['water'] or item['ingredients']['coffee'] > resources['coffee']:
            print("insufficient resources")
            resources_check = False
            return resources_check

# TODO 7: Make coffee - reduce resources.
def reduce_resources(input):
    global resources
    global resources_check
    check_resources(input)
    item = MENU[input]
    if resources_check:
        if item in ['latte', 'cappuccino']:
            resources['water'] -= item['ingredients']['water']
            resources['milk'] -= item['ingredients']['milk']
            resources['coffee'] -= item['ingredients']['coffee']
        else:
            resources['water'] -= item['ingredients']['water']
            resources['coffee'] -= item['ingredients']['coffee']
    else:
        pass



# TODO 5: Process Coins
def insert_coins():
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    total = quarters * .25 + dimes * .10 + nickles * .05 + pennies * .01
    return total

# TODO 6: Check if transaction successful
def cashier(input):
    global money
    global paid_check
    print("Please insert coins.")
    total = insert_coins()
    due = MENU[input]["cost"]
    if total > due:
        change = round(total-float(due),2)
        print(f"Here is ${change} in change")
        money += due
    else:
        print("Sorry that's not enough money. Money refunded.")
        paid_check = False
        return paid_check

def order(input):
    global resources_check
    global paid_check
    global ordering_check
    if input not in MENU:
        print("I am sorry, please try again.")
    else:
        paid_check = True
        resources_check = True
        ordering_check = True

        while resources_check and paid_check and ordering_check:
            reduce_resources(input)
            if resources_check:
                cashier(input)
                if paid_check and ordering_check:
                     print(f"Here is your {input} ☕. Enjoy!")
                     ordering_check = False
            else:
                ordering_check = False



while on:
    # TODO: 1. Ask "What would You like (espresso/latte/cappuccino)?"
    user_input = input("What would You like (espresso/latte/cappuccino)?: ")

    # TODO: 2. Turn off machine using "off"
    if user_input == "off":
        print("Goodbye.")
        on = False
    # TODO: 3. print report using "report"
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        # for item,amount in resources.items():
        #     print(f"{item.title()}: {amount}")
        print(f"Money: ${money}")
    # Complete transaction
    else:
        order(user_input)






