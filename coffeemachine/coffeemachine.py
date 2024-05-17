"""Project coffeemachine"""


class CoffeeMachine:
    """This class represents a simple coffeemachine with such functions as serving clients and giving you the
    collected money. It can serve 3 different types of coffee and needs filling once in a while."""
    def __init__(self):
        """Initialization of coffeemachine resources."""
        self.water = 400
        self.milk = 540
        self.coffee_beans = 120
        self.disposable_cups = 9
        self.money = 550
        self.state = "waiting_for_action"

    def process_input(self, user_input):
        """Processes user input based on the current state of the machine
        (such as waiting for action, choosing coffee type or being filled)
        :argument: user_input (str): user's input
        :returns: none"""
        if self.state == "waiting_for_action":
            self.process_action(user_input)
        elif self.state == "choosing_coffee":
            self.buy_coffee(int(user_input))
            self.state = "waiting_for_action"
        elif self.state == "filling":
            self.fill_supplies_prompt()
            self.state = "waiting_for_action"

    def process_action(self, action):
        """Processes user input based on the current state of the coffeemachine. There are 5 options:
        buy, fill, take, show remaining ingredients, exit.
        :arg: action (str): user's inputted action
        :returns: none"""
        if action == "buy":
            print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
            self.state = "choosing_coffee"
        elif action == "fill":
            self.state = "filling"
            self.fill_supplies_prompt()
        elif action == "take":
            self.take_money()
        elif action == "remaining":
            self.print_supplies()
        elif action == "exit":
            exit()
        else:
            print("Invalid action! Please try again.")

    def buy_coffee(self, choice):
        """Processes the purchase of one of 3 types of coffee: espresso, latte and cappuccino.
        Different types of coffee need different amount of ingredients, so the program first checks if you have
        the right amount, then proceeds brewing you a coffee.
        :arg: choice(int): 1- espresso, 2- latte, 3- cappuccino.
        :returns: none"""
        water_needed = 0
        milk_needed = 0
        coffee_beans_needed = 0
        cost = 0

        if choice == 1:  # espresso choice
            water_needed = 250
            coffee_beans_needed = 16
            cost = 4
        elif choice == 2:  # latte choice
            water_needed = 350
            milk_needed = 75
            coffee_beans_needed = 20
            cost = 7
        elif choice == 3:  # cappuccino choice
            water_needed = 200
            milk_needed = 100
            coffee_beans_needed = 12
            cost = 6

        if self.water < water_needed:
            print("Sorry, not enough water!")
        elif self.milk < milk_needed:
            print("Sorry, not enough milk!")
        elif self.coffee_beans < coffee_beans_needed:
            print("Sorry, not enough coffee beans!")
        elif self.disposable_cups < 1:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, brewing you a coffee!")
            self.water -= water_needed
            self.milk -= milk_needed
            self.coffee_beans -= coffee_beans_needed
            self.disposable_cups -= 1
            self.money += cost

    def fill_supplies_prompt(self):
        """Is used to update the machine's supplies when it runs out of some ingredient.
        :returns: none."""
        try:
            print("How many ml of water do you want to add:")
            self.water += int(input())
            print("How many ml of milk do you want to add:")
            self.milk += int(input())
            print("How many grams of coffee beans do you want to add:")
            self.coffee_beans += int(input())
            print("How many disposable cups of coffee do you want to add:")
            self.disposable_cups += int(input())
            self.state = "waiting_for_action"
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            self.fill_supplies_prompt()

    def take_money(self):
        """Gives you all the collected money from the coffeemachine
        (actually just resets the money count)
        :returns: none"""
        print(f"I gave you ${self.money}")
        self.money = 0

    def print_supplies(self):
        """Prints the current ingredients available for brewing coffee.
        :returns: none"""
        print("The coffee machine has:")
        print(f"{self.water} of water")
        print(f"{self.milk} of milk")
        print(f"{self.coffee_beans} of coffee beans")
        print(f"{self.disposable_cups} of disposable cups")
        print(f"${self.money} of money")


def main():
    """The main function that runs the coffeemachine program."""
    coffee_machine = CoffeeMachine()

    while True:
        action = input("Write action (buy, fill, take, remaining, exit): ").strip()
        coffee_machine.process_input(action)


if __name__ == "__main__":
    main()

