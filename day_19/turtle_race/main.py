from turtle import Turtle, Screen
import random

def main() -> None:
    is_race_on = False
    screen = Screen()
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
    
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    
    turtles = []
    
    for index, color in enumerate(colors):
        x = -230
        y = -50 + (index * 30)
        turtle = Turtle(shape="turtle")
        turtle.speed(4)
        turtle.color(color)
        turtle.penup()
        turtle.goto(x, y)
        turtles.append(turtle)
        
    if user_bet:
        is_race_on = True
    
    while is_race_on:
        for turtle in turtles:
            if turtle.xcor() > 230:
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    is_race_on = False
                    message = f"You Won! The {winning_color} turtle won the race!"
                else:
                    is_race_on = False
                    message = f"You lost! The {winning_color} turtle was the winner."
                turtle.home()
                turtle.write(message, align="center", font=("Arial", 16, "normal"))
            random_distance = random.randint(0, 10)
            turtle.forward(random_distance)
    
    screen.exitonclick()


if __name__ == '__main__':
    main()