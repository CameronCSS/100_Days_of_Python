from turtle import Turtle, Screen


def main() -> None:
    tim = Turtle()
    screen = Screen()
    
    def move_forwards() -> None:
        tim.forward(10)
        
    def move_backwards() -> None:
        tim.backward(10)
    
    def turn_right() -> None:
        tim.left(10)
        
    def turn_left() -> None:
        tim.right(10)
        
    def clear_drawing() -> None:
        tim.reset()
        
    
    screen.listen()
    screen.onkey(move_forwards, "w")
    screen.onkey(move_backwards, "s")
    screen.onkey(turn_right, "a")
    screen.onkey(turn_left, "d")
    screen.onkey(clear_drawing, "c")
    screen.exitonclick()


if __name__ == '__main__':
    main()