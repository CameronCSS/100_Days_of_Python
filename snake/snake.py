from turtle import Turtle

STARTING_POSITION = [(-5, -5), (-25, -5), (-45, -5)]
MOVE_DISTANCE = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self) -> None:
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.move_speed = 0.2
        
    def create_snake(self) -> None:
        for position in STARTING_POSITION:
            self.add_segment(position)
            
    def move(self) -> None:
        for seg_num in range(len(self.segments) - 1,0,-1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        
    def add_segment(self, position) -> None:
        snake_segment = Turtle("square")
        snake_segment.color("white")
        snake_segment.penup()
        snake_segment.goto(position)
        self.segments.append(snake_segment)
        
    def extend(self) -> None:
        self.add_segment(self.segments[-1].position())
        self.move_speed *= 0.9
        
        
    def left(self) -> None:
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        
    def right(self) -> None:
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        
    def up(self) -> None:
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
        
    def down(self) -> None:
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
        
    def x_cord(self) -> None:
        return self.head.xcor()
    
    def y_cord(self) -> None:
        return self.head.ycor()
    
    def write(self, message) -> None:
        self.head.clear()
        self.head.home()
        self.head.write(message, align="center", font=("Arial", 20, "normal"))
        self.head.hideturtle()  # Hide the snake head after writing the message
        
    def reset(self) -> None:
        self.head.clear()
        # Hide the segments and clear them
        for segment in self.segments:
            segment.hideturtle()  # Hide each segment before clearing
        self.segments.clear()  # Clear the list of segments
        self.create_snake()    # Recreate the snake
        self.head = self.segments[0]  # Reset the head reference
        self.move_speed = 0.2  # Reset move speed
        
        