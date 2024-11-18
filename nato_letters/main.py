import pandas as pd
import os


pwd = os.getcwd()


def main() -> None:

    data=pd.read_csv(f"{pwd}\\nato_phonetic_alphabet.csv")
    
    nato_dict = { row.letter : row.code for index, row in data.iterrows()}
    
    def generate_phonetic():
        user_word = input("Enter a word: ").upper()

        try:
            output = [nato_dict[letter] for letter in user_word]
        except:
            print("Sorry, only letters in the input please.")
            generate_phonetic()
        else:
            print(output)

    generate_phonetic()


if __name__ == '__main__':
    main()
    
    