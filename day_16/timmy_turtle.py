from turtle import Turtle, Screen

from random import random

from prettytable import PrettyTable



# timmy = Turtle()

# print(timmy)

# timmy.shape("turtle")
# timmy.color("green")


# my_screen = Screen()

# print(my_screen.canvheight)

# timmy.begin_fill()
# while True:
#     timmy.forward(200)
#     timmy.left(170)
#     if abs(timmy.pos()) < 1:
#         break

# timmy.end_fill()

# for steps in range(100):
#     for c in ('blue', 'red', 'green'):
#         timmy.color(c)
#         timmy.forward(steps)
#         timmy.right(30)


# my_screen.exitonclick()

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])

table.add_column("Type", ["Electric", "Water", "Fire"])

table.align = "l"

print(table)