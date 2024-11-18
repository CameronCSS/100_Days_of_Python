from tkinter import *
import os
import math
import win32gui
import win32con


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
WHITE = "#f5f5f7"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

timer = None
pwd = os.getcwd()


def main():

    def force_focus():
        window_name = win32gui.FindWindow(None, "Pomodoro Timer")
        if window_name:
            # If minimized, restore the window
            if win32gui.IsIconic(window_name):
                win32gui.ShowWindow(window_name, win32con.SW_RESTORE)
            # Bring window to front and focus
            win32gui.SetForegroundWindow(window_name)
            
        
    # ---------------------------- TIMER RESET ------------------------------- # 
    def reset_timer():
        window.after_cancel(timer)
        main_label.config(text="Timer", fg=GREEN)
        checkmarks.config(text=f"")
        canvas.itemconfig(timer_text, text=f"00:00")
        

    # ---------------------------- TIMER MECHANISM ------------------------------- # 
    def start_timer():
        main_label.config(text="Work", fg=GREEN)
        checkmarks.config(text=f"")
        countdown(count=WORK_MIN * 60, total_done=1)
        

    # ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
    def countdown(count, total_done):
        minutes = math.floor(count / 60)
        seconds = count % 60
        canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
        
        if count > 0:
            global timer
            timer = window.after(1000, countdown, count - 1, total_done)
        else:
            force_focus()
            
            if total_done == 8:
                start_timer()
            elif total_done == 7:
                total_done += 1
                main_label.config(text="Break", fg=RED)
                checkmarks.config(text=f"✔✔✔✔")
                countdown(count=LONG_BREAK_MIN * 60, total_done=total_done)
            elif total_done % 2 != 0:
                total_done += 1
                main_label.config(text="Break", fg=PINK)
                checkmarks.config(text=f"✔" * math.floor(total_done / 2))
                countdown(count=SHORT_BREAK_MIN * 60, total_done=total_done)
            elif total_done % 2 == 0:
                total_done += 1
                main_label.config(text="Work", fg=GREEN)
                countdown(count=WORK_MIN * 60, total_done=total_done)
            
        

    # ---------------------------- UI SETUP ------------------------------- #
    window = Tk()
    window.title("Pomodoro Timer")
    window.config(padx=100, pady=50, bg=YELLOW)


    canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
    tomato_img = PhotoImage(file=f"{pwd}\\tomato.png")
    canvas.create_image(100, 112, image=tomato_img)
    timer_text = canvas.create_text(100, 130, text="00:00", fill=WHITE, font=(FONT_NAME, 35, "bold"))
    canvas.grid(column=2, row=2)

    main_text = "Timer"

    main_label = Label(text=main_text, font=(FONT_NAME, 40, "bold"), fg=GREEN, bg=YELLOW)
    main_label.grid(column=2, row=1)

    start_button = Button(text="Start", command=start_timer, highlightthickness=0)
    start_button.grid(column=1, row=3)

    reset_button = Button(text="Reset", command=reset_timer, highlightthickness=0)
    reset_button.grid(column=3, row=3)

    checkmarks = Label(text="", font=(FONT_NAME, 10, "bold"), fg=GREEN, bg=YELLOW)
    checkmarks.grid(column=2, row=4)




    window.mainloop()




if __name__ == '__main__':
    main()