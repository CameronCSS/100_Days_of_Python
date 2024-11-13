
# Read mode and write mode!!

# with open AS filename:
    
#     readlines() instead of just read to get a list!
    
    


def main() -> None:
    with open ("day_24\\input\\names\\invited_names.txt", mode="r") as names_list:
        names = names_list.readlines()
        
    with open("day_24\\input\\letters\\starting_letter.txt", mode="r") as letter_template:
        letter = letter_template.read()
        
        letter = letter_template.red()                       
    for name in names:
        name = name.strip()
        
        new_letter = letter.replace("[name]", name)
        
        with open(f"day_24\\output\\ReadyToSend\\letter_to_{name}.txt", mode="w") as output_letter:
            output_letter.write(new_letter)  
            
            
    
if __name__ == '__main__':
    main()