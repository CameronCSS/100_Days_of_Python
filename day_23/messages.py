from turtle import Turtle


ALIGNMENT = "center"
FONT = ("Monospace", 20, "normal")

class Message(Turtle):
    
    def __init__(self, xcor, ycor) -> None:
        super().__init__()
        self.level = 1
        self.penup()
        self.goto(xcor, ycor)
        self.hideturtle()
        self.color("black")
        self.update_level()
            
    def update_level(self) -> None:
        self.clear()
        self.write(f"Level: {self.level}", align=ALIGNMENT, font=FONT)
        
    def increase_level(self) -> None:
        self.level += 1
        self.update_level()
        
    def wait_message(self, message) -> None:
        self.clear()
        self.write(f"{message}", align=ALIGNMENT, font=FONT)