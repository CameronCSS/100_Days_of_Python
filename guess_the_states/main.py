import turtle
import os
import pandas as pd
import csv


pwd = os.getcwd()


already_guessed = []
state_turtles = []

df=pd.read_csv(f"{pwd}\\50_states.csv")

states_list = df['state'].tolist()

screen = turtle.Screen()
screen.title("U.S. States Game")
image = f"{pwd}\\blank_states_img.gif"
screen.addshape(image)

us_map = turtle.Turtle()
us_map.shape(image)


while len(already_guessed) < len(states_list):
    answer_state = screen.textinput(title = f"{len(already_guessed)}/{len(states_list)} States Correct", prompt="What's another state's name?")
    

    # If the user types 'Exit', break the loop
    if answer_state == 'Exit' or answer_state is None:
        break
    
    answer_state = answer_state.title()
    
    if answer_state in already_guessed:
        new_answer = screen.textinput(title="Already Guessed", 
                                    prompt=f"You've already guessed {answer_state}! Guess Again")
        if new_answer is None or new_answer == 'Exit':
            break
        answer_state = new_answer.title()
    
    if answer_state in states_list and answer_state not in already_guessed:
        # Get index of the state (case insensitive)
        state_index = states_list.index(answer_state)
        correct_state = states_list[state_index]  # Get properly capitalized state name
        
        # Add to guessed list
        already_guessed.append(correct_state)
        
        # Get coordinates
        state_data = df[df['state'] == correct_state].iloc[0]
        
        # Create new turtle for this state
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.color("blue")
        state_turtle.goto(state_data['x'], state_data['y'])
        state_turtle.write(correct_state, align="center", font=("Arial", 8, "bold"))
        state_turtles.append(state_turtle)
    


# Game over - show missing states
if len(already_guessed) < len(states_list):
    missing_states = [state for state in states_list if state not in already_guessed]
    
    missed_df = pd.DataFrame(missing_states, columns=['Missed State'])

    missed_df.to_csv('missed_states.csv', index=False)

    # Write missing states in red
    for state in missing_states:
        state_data = df[df['state'] == state].iloc[0]
        state_turtle = turtle.Turtle()
        state_turtle.hideturtle()
        state_turtle.penup()
        state_turtle.color('red')
        state_turtle.goto(state_data['x'], state_data['y'])
        state_turtle.write(state, align="center", font=("Arial", 8, "bold"))
        

screen.exitonclick()