from menu_item import MenuItem


class Menu:
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

    def __init__(self):
        pass

    def get_items(self):
        """
        Returns all the names of the available menu items as a concatenated string.
        :return: all the names of the available menu items as a concatenated string
        """
        return "/".join(self.MENU.keys())

    def find_drink(self, order_name):
        """
        Searches the menu for a particular drink by name. Returns a MenuItem object if it exists, otherwise returns None.
        :param order_name: The name of the drinks order.
        :return: a MenuItem object if it exists, otherwise returns None.
        """
        if order_name not in self.MENU.keys():
            return None

        ingredients = self.MENU[order_name]["ingredients"]
        cost = self.MENU[order_name]["cost"]

        return MenuItem(order_name, cost, ingredients)
