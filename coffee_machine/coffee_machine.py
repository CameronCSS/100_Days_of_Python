import csv
from menu import items

emojis = {
    "espresso": "☕️",
    "latte": "🥛",
    "cappuccino": "🍵"
}

## TODO: Build type checking error catches

using_machine = True

resources = {}

with open('report.csv', 'r') as file:
    reader = csv.reader(file)
    headers = next(reader)
    values = next(reader)
    

    resources = {
        "water": int(values[0]),
        "milk": int(values[1]),
        "coffee": int(values[2]),
        "money": float(values[3]),
    }


def print_resources():
    for item in ['water', 'milk', 'coffee', 'money']:
        print(f"{item}: {resources[item]}")


def save_report():
    with open('report.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["water", "milk", "coffee", "money"])
        writer.writerow([resources["water"], resources["milk"], resources["coffee"], resources["money"]])


def get_bev(choice):
    item = items[choice]
    water_needed = item["ingredients"]["water"]   
    coffee_needed = item["ingredients"]["coffee"]
    milk_needed = item["ingredients"].get("milk", 0)
    cost = item["cost"]
    on_hand_water = resources["water"]
    on_hand_coffee = resources["coffee"]
    on_hand_milk = resources["milk"]

    if on_hand_water < water_needed:
        return print("Error: Not enough water available.")

    if on_hand_coffee < coffee_needed:
        return print("Error: Not enough coffee available.")

    if on_hand_milk < milk_needed:
        return print("Error: Not enough milk available.")

    count_coins(cost, item["ingredients"])

def count_coins(cost, ingredients):
    while True:
        quarters = int(input("How many quarters: ")) * 25
        dimes = int(input("How many dimes: ")) * 10
        nickles = int(input("How many nickels: ")) * 5
        pennies = int(input("How many pennies: "))

        paid = quarters + dimes + nickles + pennies
        dollars = paid / 100

        if dollars < cost:
            print(f"Sorry. That isn't enough money. You gave me ${dollars:.2f}, cost was ${cost:.2f}.")
            return print("Money Refunded")
        else:
            change = round((dollars - cost), 2)
            print(f"Here is your ${change:.2f} in change.")
            return give_bev(ingredients, cost)

def give_bev(ingredients, cost):
    for item, amount in ingredients.items():
        resources[item] -= amount
    resources["money"] += cost
    save_report()
    print(f"Here is your {choice} {emojis[choice]} Enjoy!")

def check_ingredients():
    for item, amount in resources.items():
        if amount == 0 and item != "money":
            print(f"Sorry. Machine is out of {item}")
            return False
    return True

def refill_ingredient(ingredient, amount):
    if ingredient in resources:
        resources[ingredient] += amount
        print(f"Added {amount} units of {ingredient}. New total: {resources[ingredient]}")
    else:
        print(f"Invalid ingredient: {ingredient}")

def refill_process():
    while True:
        refill = input("What would you like to refill? (Water/Milk/Coffee) or 'done' to finish: ").lower()
        if refill == 'done':
            save_report()
            break
        if refill in ["water", "milk", "coffee"]:
            try:
                amount = int(input(f"How much {refill} would you like to add? "))
                refill_ingredient(refill, amount)
            except ValueError:
                print("Please enter a valid number.")
        else:
            print("Invalid ingredient. Please choose Water, Milk, or Coffee.")

while using_machine:
    if not check_ingredients():
        print("Please refill the machine.")
        refill_process()
        continue

    use_it = input("Would you like to use the coffee machine? 'Y' or 'N' ").lower()

    if use_it == "report":
        print_resources()
    elif use_it == 'off':
        break
    elif use_it == 'refill':
        refill_process()
        continue
    elif use_it == 'y':
        choice = input("What would you like? (espresso/latte/cappuccino): ")
        get_bev(choice)
    elif use_it == 'n':
        using_machine = False
    else:
        print("Invalid input. Please enter 'Y' or 'N'.")