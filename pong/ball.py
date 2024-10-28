from turtle import Turtle


class Ball(Turtle):
    
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.goto(0, 0)
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1
    
    
    def move(self) -> None:
        x = self.xcor() + self.x_move
        y = self.ycor() + self.y_move
        self.goto(x,y)
        
    def bounce(self) -> None:
        self.y_move *= -1
        
    def hit(self) -> None:
        self.x_move *= -1
        self.move_speed *= 0.8
        
    def reset_position(self) -> None:
        self.goto(0, 0)
        self.x_move *= -1
        self.move_speed = 0.1
        
    def hide(self) -> None:
        self.goto(0, 800)