from tkinter import *

def main() -> None:
    def button_clicked():
        miles = float(input.get())
        km = round(miles * 1.609)
        converted_label["text"] = f"{km}"
        print("Button clicked")
        
        
    window = Tk()

    window.title("Miles to Km Converter")
    window.minsize(width=100, height=100)
    window.config(padx=20, pady=20)
    
    input = Entry(width=10)
    input.grid(column=2, row=1)
    
    miles_label = Label(font=("Arial", 10, "normal"))
    miles_label["text"] = "Miles"
    miles_label.grid(column=3, row=1)

    is_equal = Label(font=("Arial", 10, "normal"))
    is_equal["text"] = "is equal to"
    is_equal.grid(column=1, row=2)
    
    km_equal = Label(font=("Arial", 10, "normal"))
    km_equal["text"] = "Km"
    km_equal.grid(column=3, row=2)
    
    
    converted_label = Label(font=("Arial", 10, "normal"))
    converted_label["text"] = "0"
    converted_label.grid(column=2, row=2)
    
        
    button = Button(text="Calculate", command=button_clicked)
    button.grid(column=2, row=3)





    window.mainloop()
    
    

if __name__ == '__main__':
    main()