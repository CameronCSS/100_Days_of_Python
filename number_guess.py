import random
EASY = 10
HARD = 5
turns = 0

def check_answer(guess, number, turns):
    """Checks actual number against the guess. Returns number of turns remaining"""
    if guess == number:
        print(f"You got it. The answer was {number}")
    elif guess > number:
        print("Too high.")
        print("Guess again.")
        return turns - 1
    elif guess < number:
        print("Too low.")
        print("Guess again.")
        return turns - 1


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        return EASY
    elif difficulty == "hard":
        return HARD
    else:
        print("invalid option. Default is Easy (10 attempts)")
    return EASY

def game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. \n")
    number = random.randint(1, 100)

    turns = set_difficulty()

    guess = 0

    while guess != number:
        print(f"You have {turns} attempts remaining to guess the number. \n")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess, number, turns)
        if turns == 0:
            print("You ran out of turns")
            print(f" The number was {number}")
            return

play_again = True

while play_again:
    game()
    again = input("Want to play again? Type 'y' or 'n': ").lower()
    if again != 'y':
        play_again = False
        break