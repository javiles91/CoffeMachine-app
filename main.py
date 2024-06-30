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

MONEY = 0
# TODO: 1. Print report of all coffe machine resources


def offering():
    print(''' Welcome to your happy coffe machine!
    These are the options available and prices:
    1. Espresso --> $1.5
    2. Latte --> $2.5
    3. Cappuccino --> $3.0
    
    Additional instructions:
    1. To turn off the machine pleaser type: "off"
    2. To view available resources please type: "report"''')

    selecting = True
    good_options = ['espresso', 'latte', 'cappuccino', 'off', 'report']
    while selecting:
        user_selection = input('\nWhat would you like? (espresso/latte/cappuccino): ')
        if user_selection in good_options:
            return user_selection
        else:
            print('Not a valid option, please try again')


def print_report():
    for key in resources:
        print(f'{key}: {resources[key]}')
    print(f'Money: {MONEY}')


def check_availability(coffe):

    ingredients_needed = MENU[coffe]['ingredients']

    for key in ingredients_needed:
        if resources[key] - ingredients_needed[key] <= 0:

            print(f'Sorry there is no enough {key}.')
            return {'availability': False, 'na': 'na'}
    return {'availability': True, 'required_ingredients': ingredients_needed}


def payment_handler(selected_coffe):
    global MONEY
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    total = quarters * 0.25 + dimes * 0.1 + nickels * 0.05 + pennies * 0.01
    print(f'total: {total}')

    coffe_price = MENU[selected_coffe]['cost']
    remaining = round(total - coffe_price, 2)

    if remaining >= 0:
        MONEY += coffe_price
        if remaining > 0:
            print(f'Here is ${remaining} dollars in change.')
        return True
    else:
        print(f'Sorry that is not enough money. Money refunded')
        return False


def make_coffe(coffe, ingredients):

    for key in resources:
        resources[key] -= ingredients[key]

    print(f'Here is your {coffe}. Enjoy!')


# ----------------------------------------------------------------------------------------------

def main():

    repeat = True

    while repeat:
        # Offering options to user
        selection = offering()
        # Verifying option selected to follow proper path
        if selection == 'off':
            return
        elif selection == 'report':
            print_report()
            continue

        availability, required_ingredients = check_availability(selection).values()
        # if no available resources we notified the user and exit
        if not availability:
            return
        # if we have the resources we process the user payment
        payment = payment_handler(selection)

        if not payment:
            return

        make_coffe(selection, required_ingredients)


main()
