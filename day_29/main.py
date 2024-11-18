from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
from characters import letters, numbers, symbols
from datetime import datetime
import pyperclip

pwd = os.getcwd()


FONT = "Arial"
SIZE = 10
WHITE = "#f5f5f7"
BLACK = "#222222"

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
        
        # Check if any fields were left empty
        if len(website) == 0 or len(email) == 0 or len(password) == 0:
            messagebox.showerror(title="Warning", message="Please don't leave any fields empty!")
            return
        
        # Verify info with User before saving
        is_ok = messagebox.askokcancel(title=website, 
                               message=f"""These are the details entered: 
                               \nEmail: {email} \nPassword: {password} \n
                               Is it ok to save?""")
        
        if is_ok:
            with open("my_psswrds.txt", "a") as pass_file:
                pass_file.write(f"{website} | {email} | {password} | {date}\n")

            # Clear inputs
            website_input.delete(0, 'end')
            pass_input.delete(0, 'end')



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
    generate_pass = Button(text="Generate", bg=BLACK, fg=WHITE, command=generate_password)
    generate_pass.grid(column=3, row=3)
    
    add_button = Button(text="Save Password", bg=BLACK, fg=WHITE, width=36, command=save_password)
    add_button.grid(column=1, row=4, columnspan=2)



    window.mainloop()







if __name__ == '__main__':
    main()