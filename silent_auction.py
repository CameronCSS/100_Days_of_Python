import os



bidders = {
}

add_bidder = True

while add_bidder:
    os.system('cls')
    name = str(input("What is your name?: "))
    bid = int(input("What is your bid?: $"))

    bidders[name] = bid

    add = input("Are there any other bidders? Type 'yes or 'no'.")



    if add == "no":
        add_bidder = False

highest = 0
winner = ""

for k in bidders:
    if bidders[k] > highest:
        highest = bidders[k]
        winner = k

print(f"The winner is {winner} with a bid of ${highest}")