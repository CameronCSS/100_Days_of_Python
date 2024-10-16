print("*******************************************************************************")
print("          |                   |                  |                     |")
print(" _________|________________.=""_;=.______________|_____________________|_______")
print("|                   |  ,-'_,=\"\"     '\"=.|                  |")
print("|___________________|__\"=._o'\"-._        '\"=.______________|___________________")
print("          |                '\"=._o'\"=._      _'\"=._                     |")
print(" _________|_____________________:=._o \"=._.\"_.-=\"'\"=.__________________|_______")
print("|                   |    __.--\" , ; '\"=._o.\" ,-\"\"\"-._ \".   |")
print("|___________________|_._\"  ,. .' ' '' ,  '\"-._\"-._   \". '__|___________________")
print("          |           |o'\"=._' , '\" '; .\" ,  \"-._\"-._; ;              |")
print(" _________|___________| ;'-.o'\"=._; .\" ' ''.'\" . \"-._ /_______________|_______")
print("|                   | |o;    '\"-.o'\"=._''  '' \" ,__.--o;   |")
print("|___________________|_| ;     (#) '-.o '\"=.'_.--\"_o.-; ;___|___________________")
print("____/______/______/___|o;._    \"      '\".o|o_.--\"    ;o;____/______/______/____")
print("/______/______/______/\"=._o--._        ; | ;        ; ;/______/______/______/____")
print("____/______/______/______/__\"=._o--._   ;o|o;     _._;o;____/______/______/____")
print("/______/______/______/______/____\"=._o._; | ;_.--\"o.--\"_/______/______/______/__")
print("____/______/______/______/______/_____'=.o|o_.--\"\"___/______/______/______/____")
print("/______/______/______/______/______/______/______/______/______/______/_____ /")
print("*******************************************************************************")


print("Welcome to Treasure Island. \n Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?\n")

def get_valid_input(prompt, valid_options):
    while True:
        user_input = input(prompt).lower()
        if user_input in valid_options:
            return user_input
        else:
            print(f"\nInvalid input. Please type one of the following: {', '.join(valid_options)}.")



direction = get_valid_input('      Type "left" or "right": ', ['left', 'right'])

if direction == 'left':
    print("\nYou've come to a lake. There is an island in the middle of the lake.")
    
    what_do = get_valid_input('\nType "wait" to wait for a boat or "swim" to swim across: ', ['wait', 'swim'])

    if what_do == 'wait':
        print("\nYou arrive at the island unharmed. There is a house with 3 doors.")
        color = get_valid_input('\nOne red, one yellow, and one blue. Which color do you choose? ', ['red', 'yellow', 'blue'])
        if color == 'red':
            print("\nIt's a room full of fire. Game Over.")
        elif color == 'yellow':
            print("\nYou found the treasure. YOU WIN !!!.\n")
        else:
            print("\nYou enter a room of beasts. Game Over.\n")
    else:
        print("\nYou get attacked by an angry trout. Game Over.\n")
else:
    print("\nYou fell into a hole. Game Over.\n")