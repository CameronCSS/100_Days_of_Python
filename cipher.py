alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Caesar Cipher!!!")

def caesar(original_text, shift_amount, code):
    output_text = ""
    if code == "decode":
        shift_amount *= -1

    for letter in original_text:
        if letter in alphabet:

            index = alphabet.index(letter) + shift_amount
            index %= len(alphabet)

            output_text += alphabet[index]
        else:
            output_text += letter

    print(f"Here is the {code}d result: {output_text}")

should_continue = True

while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    caesar(text, shift, direction)

    restart = input("Type 'yes' if you want to go again. Otherwise, type 'no'.\n").lower()
    if restart == "no":
        should_continue = False
        print("Goodbye")


