from turtle import Turtle, Screen
from snake import Snake
from food import Food
import random
import time

def main() -> None:
    global x
    game = True
    
    screen = Screen()
    screen.setup(width=625, height=610)
    screen.bgcolor("black")
    screen.title("SNAKE")
    screen.tracer(0)

    snake = Snake()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
        
    while game:
        screen.update()
        time.sleep(0.1)
        
        snake.move()
        
        # This gets snake to edge of screen but will be problematic when it comes to grid system for food.  WIP
        
        if snake.x_cord() > 300 or snake.x_cord() < -305:
            game = False
            message = f"You lost!"
            snake.write(message)
        elif snake.y_cord() > 300 or snake.y_cord() <= -305:
            game = False
            message = f"You lost!"
            snake.write(message)
    def end_game() -> None:
        game = False
        
    
    
    screen.exitonclick()

if __name__ == '__main__':
    main()