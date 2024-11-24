from tkinter import *
from tkinter import messagebox
import os
import pandas as pd
import random

pwd = os.getcwd()


BACKGROUND_COLOR = "#B1DDC6"
FONT = "Arial"
WHITE = "#f5f5f7"
BLACK = "#222222"

try:
    words_df = pd.read_excel(f"{pwd}\\data\\words_to_learn.xlsx") # csv doesnt work for japanese character encoding
except FileNotFoundError:
    words_df = pd.read_excel(f"{pwd}\\data\\japanese_words.xlsx")

words_dict = words_df.to_dict('records')
current_card = {}


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    try:
        current_card = random.choice(words_dict)

        canvas.itemconfig(card_title, text="Japanese", fill=BLACK)
        canvas.itemconfig(kanji_text, text=current_card['Kanji'], fill=BLACK)
        canvas.itemconfig(romaji_text, text=current_card['Romaji'], fill=BLACK)
        
        canvas.itemconfig(canvas_image, image=card_img)
        
        flip_timer = window.after(5000, func=flip_card)
        
    except:
        canvas.itemconfig(card_title, text="DONE for Today", fill="green")
        canvas.itemconfig(kanji_text, text="")
        canvas.itemconfig(romaji_text, text="")
    
def flip_card():
    global current_card, flip_timer
    canvas.itemconfig(canvas_image, image=answer_img)

    canvas.itemconfig(card_title, text="English", fill=WHITE)
    canvas.itemconfig(kanji_text, text=current_card['English'], fill=WHITE)
    canvas.itemconfig(romaji_text, text=current_card['Romaji'], fill=WHITE)
    
def is_known():
    words_dict.remove(current_card)
    
    word_list = pd.DataFrame(words_dict)
    word_list.to_excel(f"{pwd}\\data\\words_to_learn.xlsx", index=False)
    
    next_card()


# Window 
window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_img = PhotoImage(file=f"{pwd}\\images\\card_front.png")
answer_img = PhotoImage(file=f"{pwd}\\images\\card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_img)
canvas.grid(column=0, row=0, columnspan=2)

# Title
card_title = canvas.create_text(400, 150, text="Japanese", font=(FONT, 40, "italic"))

# word
kanji_text = canvas.create_text(400, 250, text="", font=(FONT, 40, "bold"))
romaji_text = canvas.create_text(400, 350, text="", font=(FONT, 40, "bold"))



# Buttons
wrong_image = PhotoImage(file=f"{pwd}\\images\\wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(column=0, row=1)

right_image = PhotoImage(file=f"{pwd}\\images\\right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(column=1, row=1)


next_card()



window.mainloop()