from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
from characters import letters, numbers, symbols
from datetime import datetime
import pyperclip
import json

pwd = os.getcwd()


FONT = "Arial"
SIZE = 10
WHITE = "#f5f5f7"
BLACK = "#222222"
PASS_FILENAME = "psswrds.json"

def main() -> None:


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
    def generate_password() -> None:
        # Clear input
        pass_input.delete(0, 'end')
        
        pass_letters = [choice(letters) for _ in range(randint(6,10))]
        pass_symbols = [choice(symbols) for _ in range(randint(2,4))]
        pass_numbers = [choice(numbers) for _ in range(randint(2,4))]

        password_list = pass_letters + pass_symbols + pass_numbers

        shuffle(password_list)

        password = ''.join(password_list)
        
        pass_input.insert(0, f"{password}")
        
        # Call pyperclip to automatically copy our password to the windows clipboard
        pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
    def save_password():
        website = website_input.get().title()
        email = email_input.get()
        password = pass_input.get()
        date = datetime.today().strftime('%Y-%m-%d')
        
        new_data = {
            website: {
                "email": email,
                "password": password,
                "date": date
            }
        }
        
        # Check if any fields were left empty
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Warning", message="Please don't leave any fields empty!")
        else:
            try:
                with open(PASS_FILENAME, "r") as pass_file:
                    # read old data
                    data = json.load(pass_file)
            except FileNotFoundError:
                with open(PASS_FILENAME, "w") as pass_file:
                    # Save new data
                    json.dump(new_data, pass_file, indent=4)
                    
            # Once file exists update data
            else:
                # Update old data with new data
                data.update(new_data)
                    
                with open(PASS_FILENAME, "w") as pass_file:
                    # Save updated data
                    json.dump(data, pass_file, indent=4)
                
            finally:
                # Clear inputs
                website_input.delete(0, 'end')
                pass_input.delete(0, 'end')

# ---------------------------- Search for Password ------------------------------- #
    def search_password():
        website = website_input.get().title()
        try:
            # Check if pass_file exists
            with open(PASS_FILENAME, "r") as pass_file:
                pass
        except FileNotFoundError:
            messagebox.showerror(title="No such File", message=f"Could not find '{PASS_FILENAME}'")
            
        else:
            with open(PASS_FILENAME, "r") as pass_file:
                data = json.load(pass_file)
                try:
                    email = data[website]["email"]
                    password = data[website]["password"]
                    if website in data:
                        messagebox.showinfo(title=f"{website} password", message=f"Email: {email} \nPassword: {password} \n \n(Password copied to clipboard)")
                        # Call pyperclip to automatically copy our password to the windows clipboard
                        pyperclip.copy(password)
                except:
                    messagebox.showerror(title=website, message=f"No information found for {website}")


# ---------------------------- UI SETUP ------------------------------- #
    # Window 
    window = Tk()
    window.title("Password Manager")
    window.config(padx=50, pady=50, bg=BLACK)

    # Canvas
    canvas = Canvas(width=200, height=200, bg=BLACK, highlightthickness=0)
    lock_img = PhotoImage(file=f"{pwd}\\logo.png")
    canvas.create_image(100, 100, image=lock_img)
    canvas.grid(column=1, row=0)
    
    
    # Website
    website_label = Label(text="Website: ", font=(FONT, SIZE, "normal"), bg=BLACK, fg=WHITE)
    website_label.grid(column=0, row=1, sticky="e", padx=10)
    
    website_input = Entry(width=35)
    website_input.grid(column=1, row=1, columnspan=2)
    website_input.focus()
    
    # Email
    email_label = Label(text="Email/Username: ", font=(FONT, SIZE, "normal"), bg=BLACK, fg=WHITE)
    email_label.grid(column=0, row=2, sticky="e", padx=10)
    
    email_input = Entry(width=35)
    email_input.grid(column=1, row=2, columnspan=2)
    # Fill in your email so its already in the form
    email_input.insert(0, "myemail@gmail.com")
    
    # Password
    pass_label = Label(text="Password: ", font=(FONT, SIZE, "normal"), bg=BLACK, fg=WHITE)
    pass_label.grid(column=0, row=3, sticky="e", padx=10)
    
    pass_input = Entry(width=30)
    pass_input.grid(column=1, row=3)
    
    
    # Buttons
    search_pass = Button(text="Search", bg=BLACK, fg=WHITE, width=15, command=search_password)
    search_pass.grid(column=3, row=1)
    
    generate_pass = Button(text="Generate", bg=BLACK, fg=WHITE, width=15,command=generate_password)
    generate_pass.grid(column=3, row=3)
    
    add_button = Button(text="Save Password", bg=BLACK, fg=WHITE, width=36, command=save_password)
    add_button.grid(column=1, row=4, columnspan=2)



    window.mainloop()






if __name__ == '__main__':
    main()