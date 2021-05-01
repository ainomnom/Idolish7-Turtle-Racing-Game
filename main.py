from turtle import Turtle, Screen
from random import randint

turtles = {"black": {"name": "Iori", "position": 1},
           "green":{"name": "Yamato", "position": 2},
           "orange": {"name": "Mitsuki", "position": 3},
           "red": {"name": "Riku", "position": 4},
           "CadetBlue2": {"name": "Tamaki", "position": 5},
           "purple": {"name": "Sougo", "position": 6},
           "yellow": {"name": "Nagi", "position": 7}}

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a name\n"
                                                          "(Iori/Yamato/Mitsuki/Tamaki/Sougo/Nagi/Riku): ").title()

all_turtles = []
for _ in turtles:
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.color(_)
    new_turtle.goto(x=-230, y=-75 + turtles[_]["position"] * 25)
    all_turtles.append(new_turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        if turtle.xcor() >= 215:
            race_is_on = False
            winning_color = turtle.pencolor()
            if turtles[winning_color]["name"] == user_bet:
                print(f"You've won! The winner is {turtles[winning_color]['name']}.")
            else:
                print(f"You've lost! The winner is {turtles[winning_color]['name']}.")
        random_distance = randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
