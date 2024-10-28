from turtle import Screen
from paddles import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

def main() -> None:
    game = True
    play_to_score = 5
    screen = Screen()
    screen.setup(width=800, height=600)
    screen.bgcolor("black")
    screen.title("PONG")
    screen.tracer(0)
    ball = Ball()
    l_scoreboard = Scoreboard(-100, 220)
    r_scoreboard = Scoreboard(100, 220)
    
    r_paddle = Paddle(350)
    l_paddle = Paddle(-350)
    
    screen.onkeypress(r_paddle.move_up, "Up")
    screen.onkeypress(r_paddle.move_down, "Down")
    screen.onkeypress(l_paddle.move_up, "w")
    screen.onkeypress(l_paddle.move_down, "s")

    screen.listen()
    
    while game:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()
        if ball.ycor() > 280 or ball.ycor() < -280:
            ball.bounce()
            
            
        # Way over complicated ball coordinate system to detect collisions because I was getting glitches when you hit edge of paddle and it would slingshot the ball away.
        PADDLE_HEIGHT = 120
        if (ball.xcor() > 340 and ball.xcor() < 360) and (ball.ycor() < r_paddle.ycor() + PADDLE_HEIGHT / 2 and ball.ycor() > r_paddle.ycor() - PADDLE_HEIGHT / 2):
            ball.hit()
        elif (ball.xcor() < -340 and ball.xcor() > -360) and (ball.ycor() < l_paddle.ycor() + PADDLE_HEIGHT / 2 and ball.ycor() > l_paddle.ycor() - PADDLE_HEIGHT / 2):
            ball.hit()
    
        if ball.xcor() > 380:
            ball.reset_position()
            l_scoreboard.increase_score()
            
            
        if ball.xcor() < -380:
            ball.reset_position()
            r_scoreboard.increase_score()
            
        if l_scoreboard.score == play_to_score or r_scoreboard.score == play_to_score:
            winner = Scoreboard(0, 0)
            if l_scoreboard.score > r_scoreboard.score:
                winner.winner("Left Player Wins!")
            else:
                winner.winner("Right Player Wins!")   
            ball.hide()
            screen.update()
            game = False

            
    screen.exitonclick()



if __name__ == '__main__':
    main()