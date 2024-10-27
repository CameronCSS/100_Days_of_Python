from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.color("white")
        self.update_score()
            
    def update_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self) -> None:
        self.score += 10
        self.update_score()