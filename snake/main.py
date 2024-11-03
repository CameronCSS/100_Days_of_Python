from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data import Database
import time
import tkinter as tk

def main() -> None:
    game = True
    apple_color_changed = False
    
    # Create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SNAKE")
    screen.tracer(0)

    # Initialize game objects
    snake = Snake()
    apple = Food()
    scoreboard = Scoreboard()
    
    # Key bindings
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    def game_loop():
        nonlocal game, apple_color_changed
        
        if not game:
            return
            
        screen.update()
        time.sleep(snake.move_speed)
        
        snake.move()

        # Check if the score is a multiple of 50
        if scoreboard.score > 0 and scoreboard.score % 50 == 0 and not apple_color_changed:
            apple.change_color()
            apple_color_changed = True
            
        # Reset the flag when score is no longer a multiple of 50
        if scoreboard.score > 0 and scoreboard.score % 50 != 0:
            apple_color_changed = False
            
        if snake.head.distance(apple) < 15:
            apple.refresh()
            snake.extend()
            scoreboard.increase_score()
            
        for segment in snake.segments[1:]:
            if snake.head.distance(segment) < 10:
                game_over()
                return
        
        if snake.x_cord() > 290 or snake.x_cord() < -290 or snake.y_cord() > 290 or snake.y_cord() < -290:
            game_over()
            return
            
        # Call the game_loop again using ontimer
        screen.ontimer(game_loop, 100)

    def game_over():
        nonlocal game
        game = False
        message = "GAME OVER"
        snake.write(message)  # Assuming snake has a write method for displaying text
        Database.insert_score(scoreboard.score)
    
    # Start the game loop
    game_loop()
    
    # Start the screen's main event loop
    screen.mainloop()

if __name__ == '__main__':
    main()
