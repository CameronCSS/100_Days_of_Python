from turtle import Turtle
import random


COLORS = ["yellow", "green", "red", "blue", "orange", "purple"]

class Cars(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.setheading(180)
        self.shapesize(stretch_wid = 1, stretch_len = 2)
        self.goto(360, random.randint(-250, 250))
        
    def move(self) -> None:
        self.forward(10)
        