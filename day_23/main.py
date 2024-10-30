from frog import Frog
from cars import Cars
from messages import Message
from turtle import Screen
import time


def main() -> None:
    game = True
    screen = Screen()
    screen.title("FROGGER")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    level = Message(-200,250)
    level.update_level()
    wait = Message(0,0)
    wait.wait_message("Wait for cars...")
    frog = Frog()
    speed = 0.1
    cars = []
    loop_counter = 0
    screen.listen()
    frog_can_move = False

    def move_frog():
        if frog_can_move:
            frog.move()

    screen.onkeypress(move_frog, "Up")

    # Start the game loop
    while game:
        time.sleep(speed)
        screen.update()

        # Allow the frog to move if there are enough cars
        if len(cars) > 5:
            frog_can_move = True
            wait.clear()
            
        for car in cars:
            car.move()
            
            # Detect collision
            if frog.distance(car) < 20:  # Adjust the threshold as needed
                game = False
                frog.splat()
                died = Message(0,0)
                died.color("red")
                died.wait_message("YOU DIED!!")
                screen.update()

        loop_counter += 1
        if loop_counter % 6 == 0:
            new_car = Cars()
            cars.append(new_car)
            
        if frog.ycor() > 280:
            frog.new_level()
            level.increase_level()
            speed *= 0.7
            

    screen.exitonclick()

if __name__ == '__main__':
    main()
