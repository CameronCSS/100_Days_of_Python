from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
from data import Database
import time

def main() -> None:
    game = True
    apple_color_changed = False
    button_active = False  # Track if button is active
    
    # Create screen
    screen = Screen()
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("SNAKE")
    screen.tracer(0)

    # Create button turtle
    button_turtle = Turtle()
    button_turtle.hideturtle()
    button_turtle.speed(0)
    
    # Create text turtle for button
    text_turtle = Turtle()
    text_turtle.hideturtle()
    text_turtle.speed(0)

    def draw_button():
        # Draw button background
        button_turtle.clear()
        button_turtle.penup()
        button_turtle.color("white", "green")  # white border, green fill
        button_turtle.goto(-60, -50)  # Position the button
        button_turtle.pendown()
        button_turtle.begin_fill()
        for _ in range(2):
            button_turtle.forward(120)  # Button width
            button_turtle.left(90)
            button_turtle.forward(40)   # Button height
            button_turtle.left(90)
        button_turtle.end_fill()
        
        # Draw button text
        text_turtle.clear()
        text_turtle.penup()
        text_turtle.color("white")
        text_turtle.goto(0, -35)  # Center text in button
        text_turtle.write("Play Again", align="center", font=("Arial", 14, "bold"))

    # Function to check if click is within button area
    def is_inside_button(x, y):
        nonlocal button_active
        if button_active and -60 <= x <= 60 and -50 <= y <= -10:
            button_action()

    # Set up click listener
    screen.onscreenclick(is_inside_button)

    # Initialize game objects
    snake = Snake()
    apple = Food()
    scoreboard = Scoreboard()
    Database.create_db()

    # Key bindings
    screen.listen()
    screen.onkey(snake.up, "Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.left, "Left")
    screen.onkey(snake.right, "Right")
    
    def button_action():
        nonlocal game, button_active
        if button_active:  # Only respond if button is active
            game = True
            button_active = False
            button_turtle.clear()  # Clear button
            text_turtle.clear()    # Clear button text
            scoreboard.reset()     # Reset scoreboard
            snake.reset()          # Reset snake
            apple.refresh()        # Reset apple position
            game_loop()           # Restart game loop

    def game_loop():
        nonlocal game, apple_color_changed, button_active
        
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
            
        screen.ontimer(game_loop, 100)

    def game_over():
        nonlocal game, button_active
        game = False
        button_active = True  # Activate button
        message = "GAME OVER"
        snake.write(message)
        scoreboard.check_high_score()
        Database.insert_score(scoreboard.score)
        draw_button()  # Draw the button
        screen.update()  # Update screen to show button immediately

    # Start the game loop
    game_loop()
    
    # Start the screen's main event loop
    screen.mainloop()

if __name__ == '__main__':
    main()