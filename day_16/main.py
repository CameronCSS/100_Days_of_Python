from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main() -> None:
    coffee_maker = CoffeeMaker()
    menu = Menu()
    money_machine = MoneyMachine()
    

    while True:
        choice = input(f"What would you like? ({menu.get_items()})")
        if choice == 'report':
            coffee_maker.report()
            money_machine.report()
            continue
        elif choice == 'off':
            return
        
        drink = menu.find_drink(choice)
        if drink:
            pass
        else:
            continue

        if coffee_maker.is_resource_sufficient(drink):
            if money_machine.make_payment(drink.cost):
                coffee_maker.make_coffee(drink)
        else:
            continue


if __name__ == '__main__':
    main()

