import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def who_won(player_score, pc_score, player_cards, pc_cards):
    print("\n")
    print(f"Your final hand: {player_cards}, final score: {player_score}")
    print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")

    if pc_score == 21:
        print("You lose, opponent has Blackjack 😱")
    elif player_score == 21:
        print("You got Blackjack 😱 YOU WIN!!")

    elif player_score > 21:
        for i in range(len(player_cards)):
            if player_cards[i] == 11:  # Check if the card is an Ace
                player_cards[i] = 1  # Replace Ace with 1
                player_score = sum(player_cards)  # Recalculate the score
                if player_score <= 21:  # If score is now valid, break the loop
                    who_won(player_score, pc_score, player_cards, pc_cards)
                else:
                    print("You went over. You lose 😭")

    elif pc_score > 21:
        print("Opponent went over. You win 😁")
    elif player_score < pc_score:
        print("You lose 😤")
    elif player_score == pc_score:
        print("Draw 🙃")
    elif player_score > pc_score:
        print("You win 😃")

play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

while play_again == 'y':
    player_cards = random.sample(cards, 2)
    player_score = sum(player_cards)
    pc_cards = random.sample(cards, 2)
    pc_score = sum(pc_cards)


    while True:
        print(f"Your cards: {player_cards}, current score: {player_score}")
        print(f"Computer's first card: {pc_cards[0]}")

        if player_score >= 21:
            break

        if pc_score >= 21:
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()

        if another_card == 'y':
            player_cards.append(random.choice(cards))
            player_score = sum(player_cards)
        elif another_card == 'n':
            while pc_score < 17:
                pc_cards.append(random.choice(cards))
                pc_score = sum(pc_cards)
            break

    who_won(player_score, pc_score, player_cards, pc_cards)

    play_again = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()


