from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# creating objects for each class
menu_o = Menu()
coffee_maker_o = CoffeeMaker()
money_machine_o = MoneyMachine()


def coffee_machine():
    # TODO 1.Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
    machine_start = True
    options = menu_o.get_items()
    while machine_start:
        response = input(f' What would you like? ({options}): ')

        if response == 'report':
            # TODO 3.Print report.
            coffee_maker_o.report()
            money_machine_o.report()
        elif response in menu_o.get_items().split('/') and not response == '':
            # TODO 4.Check resources sufficient?
            drink = menu_o.find_drink(response)
            if coffee_maker_o.is_resource_sufficient(drink):
                # TODO 5.Process coins.
                # TODO 6.Check transaction successful?
                if money_machine_o.make_payment(drink.cost):
                    # TODO 7.Make Coffee
                    coffee_maker_o.make_coffee(drink)
        else:
            # TODO 2.Turn off the Coffee Machine by entering “ off ” to the prompt.
            if response == 'off':
                return
            else:
                print('Enter a valid keyword')


coffee_machine()
