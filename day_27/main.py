from tkinter import *


# This is a test project just to get familair with Tkinter config and usecases


def main() -> None:
    def button_clicked():

        my_label["text"] = f"Hello, {input.get().title()}"
        print("Button clicked")
        
    def text_clear():

        my_label["text"] = f"Waiting for new name..."
        print("Text clicked")
        
        
    window = Tk()

    window.title("Greeter Program")
    window.minsize(width=400, height=400)
    window.config(padx=50, pady=50)
    
    input = Entry(width=10)
    input.grid(column=4, row=3)
    
    my_label = Label(font=("Arial", 20, "normal"))
    my_label.grid(column=1, row=1)
    my_label.config(padx=50, pady=50)

    my_label["text"] = "Waiting for name..."
    
        
    button = Button(text="Greet", command=button_clicked)
    button.grid(column=2, row=2)
    
    
    new_button = Button(text="Clear", command=text_clear)
    new_button.grid(column=3, row=1)





    window.mainloop()
    
    

if __name__ == '__main__':
    main()