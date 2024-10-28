from turtle import Turtle

class Paddle(Turtle):
    
    def __init__(self, x) -> None:
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(x, 0)
        self.shapesize(stretch_wid = 5, stretch_len = 1)
        
    
    def move_up(self) -> None:
        new_y = self.ycor() + 20
        cur_x = self.xcor()
        self.goto(cur_x, new_y)
        
        
    def move_down(self) -> None:
        new_y = self.ycor() - 20
        cur_x = self.xcor()
        self.goto(cur_x, new_y)