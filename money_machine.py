class MoneyMachine:
    profit = 0

    def __get_quarters(self):
        return int(input("how many quarters?: "))

    def __get_dimes(self):
        return int(input("how many dimes?: "))

    def __get_nickels(self):
        return int(input("how many nickels?: "))

    def __get_pennies(self):
        return int(input("how many pennies?: "))

    def __process_coins(self):
        """
        Returns the total amount of coins calculated by number of quarters, dimes, nickels, and pennies
        :return: total of coins inserted by the user
        """
        print("Please insert coins.")
        quarters = self.__get_quarters()
        dimes = self.__get_dimes()
        nickels = self.__get_nickels()
        pennies = self.__get_pennies()
        return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    def report(self):
        print(f"Money: {self.profit}")

    def make_payment(self, cost):
        """
        Returns True when payment is accepted, or False if insufficient.
        :param cost: The cost of the drink
        :return: True when payment is accepted, or False if insufficient.
        """
        money_received = self.__process_coins()
        if cost > money_received:
            print("Sorry that's not enough money. Money refunded.")
            return False
        self.profit += cost
        change = money_received - cost
        if change > 0:
            print(f"Here is ${str(round(change, 2))} in change.")
        return True
