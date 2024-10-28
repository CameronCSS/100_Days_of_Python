from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Monospace", 50, "normal")
WIN_FONT = ("Arial", 40, "normal")
class Scoreboard(Turtle):
    
    def __init__(self, xcor, ycor) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(xcor, ycor)
        self.hideturtle()
        self.color("white")
        self.update_score()
            
    def update_score(self) -> None:
        self.clear()
        self.write(f"{self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self) -> None:
        self.score += 1
        self.update_score()
        
    def winner(self, message) -> None:
        self.clear()
        self.write(f"{message}", align=ALIGNMENT, font=WIN_FONT)