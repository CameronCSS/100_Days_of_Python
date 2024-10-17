from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main() -> None:
    pass


def upper_everything(elements: list[str]) -> list[str]:
    return [element.upper() for element in elements]


list_1: list[str] = upper_everything(['mario', 'james', 'sandra'])

print(list_1)

if __name__ == '__main__':
    main()