from turtle import Turtle
from data import Database

ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")

class Scoreboard(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.score = 0
        self.high_score = Database.get_top_score()
        self.penup()
        self.goto(0, 270)
        self.hideturtle()  # Start hidden
        self.color("white")
        self.update_score()
        
    def update_score(self) -> None:
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        
    def increase_score(self) -> None:
        self.score += 10
        self.update_score()
        
    def check_high_score(self) -> None:
        if self.score > self.high_score:
            self.high_score = self.score
            Database.update_high_score(self.high_score)  # Update high score in the database

    def reset(self) -> None:
        self.score = 0
        self.showturtle()  # Ensure scoreboard is visible
        self.update_score()  # Update to show reset score
