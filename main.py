import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
print(all_states)
correct_answer = []
end_of_game = True
while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 States Correct",
                                    prompt="What's another state's name?")
    title_answer = answer_state.title()
    if title_answer == "Exit":
        missing_state = []
        for state in all_states:
            if state not in correct_answer:
                missing_state.append(state)
        df = pandas.DataFrame(missing_state)
        df.to_csv("states_to_learn.csv")
        break
    if title_answer in all_states:
        state_info = data[data.state == title_answer]
        x = int(state_info.x.item())
        y = int(state_info.y.item())
        correct_answer.append(title_answer)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(x, y)
        t.write(f"{title_answer}")

# states_to_learn.csv
# set_states = set(all_states)
# set_answers = (set(correct_answer))
# states_to_learn = list(set_states.difference(set_answers))
# df = pandas.DataFrame({"state_name": states_to_learn})
# df.to_csv("states_to_learn.csv")
# print(states_to_learn)
