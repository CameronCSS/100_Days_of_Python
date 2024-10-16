print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").upper()
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0


if size == 'S':
    bill += 15
    if pepperoni == 'Y':
        bill += 2 
elif size == 'M':
    bill += 20
    if pepperoni == 'Y':
        bill += 3
elif size == 'L': 
    bill += 25
    if pepperoni == 'Y':
        bill += 3
else:
    print("You tpyed an incorrect size")
    bill = 999

if bill == 999:
    print("Please try again")
else:
    if extra_cheese == 'Y':
        final_bill = bill + 1
        print(f"Your final bill is ${final_bill}")
    else:
        final_bill = bill
        print(f"Your final bill is ${final_bill}")
