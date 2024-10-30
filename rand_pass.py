import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!\n")



nr_letters = random.randrange(5,7)
nr_symbols = random.randrange(2,5)
nr_numbers = random.randrange(3,5)


password_list = []

for i in range(0, nr_letters):
    password_list.append(random.choice(letters))

for i in range(0, nr_numbers):
    password_list.append(random.choice(numbers))

for i in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

password = ''.join(password_list)

print(f"Random password is: \n {password}")