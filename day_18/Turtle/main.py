import turtle as t
from turtle import Screen
import random

def main() -> None:
    tim = t.Turtle()
    tim.speed("fastest")
    tim.shape("turtle")
    tim.color("#BADA55")
    
    # # Draw a dashed line
    # for _ in range(10):
    #     tim.forward(10)
    #     tim.penup()
    #     tim.forward(10)
    #     tim.pendown()
    
    # # Draw Shapes with random color
    # colors = ["Black", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen", "Red", "Blue", "#BADA55"]
    
    # def draw_shape(num_sides) -> None:
    #     angle = 360 / num_sides
    #     for _ in range(num_sides):
    #         tim.forward(100)
    #         tim.right(angle)
            
    # for shape_sides in range(3,11):
    #     tim.color(random.choice(colors))
    #     draw_shape(shape_sides)
    
    # directions = [0, 90, 180, 270]

    # # Random Walk Turtle
    # tim.shape("circle")
    # tim.pensize(10)
    # tim.forward(30)
    
    # Using a Random color instead of a pre-determined list of colors that you randomly pick from
    t.colormode(255)
    def random_color() -> tuple:
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)
    
    # Perform a random walk a random number of times (between 150, 300)
    # for _ in range(random.randint(100,300)):
    #     new_dir = random.choice(directions)
    #     tim.setheading(new_dir)
    #     tim.forward(30)
    #     tim.color(random_color())
    

    def draw_spirograph(size_of_gap) -> None:
        for _ in range(int(360 / size_of_gap)):
            tim.pensize(1)
            tim.circle(100)
            tim.right(size_of_gap)
            tim.color(random_color())
    
    gap = int(input("How tight do you want the circle gap?" ))
    draw_spirograph(gap)
    
    
    
    
    screen = Screen()
    screen.exitonclick()
    
    
if __name__ == '__main__':
    main()