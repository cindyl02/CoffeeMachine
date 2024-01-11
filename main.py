from money_machine import MoneyMachine
from coffee_maker import CoffeeMaker
from menu import Menu


def get_order():
    return input("What would you like? (espresso/latte/cappuccino): ")


def start_coffee_machine():
    coffee_maker = CoffeeMaker()
    money_machine = MoneyMachine()
    menu = Menu()

    should_continue = True
    while should_continue:
        order_name = get_order()
        if order_name == "off":
            should_continue = False
        elif order_name == "report":
            coffee_maker.report()
            money_machine.report()
        else:
            order = menu.find_drink(order_name)
            if order and coffee_maker.is_resource_sufficient(order) and money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)


if __name__ == '__main__':
    start_coffee_machine()
