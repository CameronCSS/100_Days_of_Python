import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

ascii = [rock, paper, scissors]


while True:
    choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
    if choice in ['0','1','2']:
        choice = int(choice)
        break
    else:
        print("Please enter a valid input.\n")

pc_choice = random.randint(0,2)

print(f"{ascii[choice]}")
print(f"Computer chose: {ascii[pc_choice]}")

if choice == pc_choice:
    result = "It's a draw!"
elif (choice == 0 and pc_choice == 2) or (choice == 1 and pc_choice == 0) or (choice == 2 and pc_choice == 1):
    result = "You win!"
else:
    result = "You lose!"

print(result)
