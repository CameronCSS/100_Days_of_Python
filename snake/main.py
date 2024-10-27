from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import random
import time

def main() -> None:
    global x
    game = True
    
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SNAKE")
    screen.tracer(0)

    snake = Snake()
    apple = Food()
    scoreboard = Scoreboard()
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
        
    while game:
        screen.update()
        time.sleep(0.1)
        
        snake.move()
        
        if snake.head.distance(apple) < 15:
            apple.refresh()
            snake.extend()
            scoreboard.increase_score()
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game = False
                message = f"GAME OVER"
                snake.write(message)
        
        if snake.x_cord() > 290 or snake.x_cord() < -290 or snake.y_cord() > 290 or snake.y_cord() < -290:
            game = False
            message = f"GAME OVER"
            snake.write(message)
            
               
    screen.exitonclick()

if __name__ == '__main__':
    main()