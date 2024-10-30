from turtle import Turtle   


class Frog(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.goto(0,-280)

    def move(self) -> None:
        self.forward(20)
    
    def splat(self) -> None:
        self.shape("circle")
        self.shapesize(stretch_wid = 1.5, stretch_len = 1.5)
        self.color("red")
        
    def new_level(self) -> None:
        self.goto(0,-280)