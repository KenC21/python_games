import turtle
import pandas
from scoreboard import Scoreboard

screen = turtle.Screen()
image = "blank_states_img.gif"
screen.title("U.S. States Game")
screen.addshape(image)
turtle.shape(image)



states_read = pandas.read_csv("50_states.csv")

answer_board = Scoreboard()

game_is_on = True
guess_list = []
score_record = 0
not_guess = []


def state_guesser():

    score = 0

    for state in states_read["state"]:
        if answer_state in state:
            coordinates = states_read[states_read["state"] == state]
            x_cor = int(coordinates.x)
            y_cor = int(coordinates.y)
            answer_board.move_answer(x_cor, y_cor, state)
            guess_list.append(state)
            score += 1
    return score


while game_is_on:

    answer_state = screen.textinput(title=f"Guess the State Score: {score_record}", prompt="What's another state name: ").title()
    if answer_state == "Exit":
        break
    if answer_state in guess_list:
        print("you already guess")
    else:
        score_record = state_guesser()


for state in states_read["state"]:
    if state not in guess_list:
        not_guess.append(state)

for_csv = pandas.DataFrame(not_guess)
for_csv.to_csv("not guess states.csv")

