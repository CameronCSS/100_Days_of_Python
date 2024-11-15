import pandas as pd
import os


pwd = os.getcwd()


def main() -> None:

    data=pd.read_csv(f"{pwd}\\nato_phonetic_alphabet.csv")
    
    nato_dict = { row.letter : row.code for index, row in data.iterrows()}
    
    user_word = input("Enter a word: ").upper()

    output = [nato_dict[letter] if letter in nato_dict else 'Not found' for letter in user_word]
    
    print(output)

if __name__ == '__main__':
    main()
    
    