class CoffeeMaker:
    resources = {
        "water": 300,
        "milk": 200,
        "coffee": 100,
    }

    def report(self):
        """
        Prints a report including amount of water, milk and coffee left and the amount of profit.
        """
        for resource, amount in self.resources.items():
            if resource == "coffee":
                units = "g"
            else:
                units = "ml"
            print(f"{resource.title()}: {amount}{units}")

    def is_resource_sufficient(self, drink):
        """
        Checks if there is enough ingredients to make the drink and returns true if there is enough. Otherwise, returns false.
        :param drink: The MenuItem object to make
        :return: boolean value True or False if there is enough ingredients to make the coffee
        """
        for resource, amount in drink.ingredients.items():
            if amount > self.resources[resource]:
                print(f"Sorry there is not enough {resource}")
                return False
        return True

    def make_coffee(self, order):
        """
        Deducts the required ingredients from the resources.
        :param order: The MenuItem object to make
        """
        for resource, amount in order.ingredients.items():
            self.resources[resource] -= amount
        print(f"Here is your {order.name} ☕️. Enjoy!")
