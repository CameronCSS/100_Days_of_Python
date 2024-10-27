from turtle import Turtle
import random

class Food(Turtle):
    
    def __init__(self) -> None:
            super().__init__()
            self.shape("circle")
            self.penup()
            self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
            self.color("green")
            self.speed("fastest")
            self.home()
            self.refresh()
            
            
    def refresh(self) -> None:
        rand_x = random.randint(-280, 280)
        rand_y = random.randint(-280, 280)
        self.goto(rand_x, rand_y)