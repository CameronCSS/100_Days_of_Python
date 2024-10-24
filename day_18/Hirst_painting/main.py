import colorgram
import os
import turtle as t
from turtle import Screen
import random

pwd = os.getcwd()

def main() -> None:
    
    # Use this to read colors out of image.jpg and build the color_list
    def extract_colors() -> list:
        rgb_list = []
        colors = colorgram.extract(pwd + "\image.jpg", 30)
        
        for color in colors:
            r = color.rgb.r
            g = color.rgb.g
            b = color.rgb.b
            new_color = (r, g, b)
            rgb_list.append(new_color)
        return rgb_list
    
    
    # Use the extract color function to build a new list
    colors_list = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74), (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153), (176, 192, 208), (168, 99, 102)]

    
    t.colormode(255)
    brush = t.Turtle()
    brush.speed("fastest")
    brush.shape("arrow")
    brush.pensize(20)
    brush.penup()
    brush.hideturtle()
    

    def random_color() -> tuple:
        """Returns a RGB value as a tuple"""
        return random.choice(colors_list)

    def make_painting() -> None:
        x, y = -200, -200
        for _ in range(10):
            y += 50
            brush.teleport(x, y)
            for _ in range(10):
                brush.dot(20, random_color())
                brush.forward(50)
    
    
    make_painting()
    
    screen = Screen()
    screen.exitonclick()
    

if __name__ == '__main__':
    main()
    
