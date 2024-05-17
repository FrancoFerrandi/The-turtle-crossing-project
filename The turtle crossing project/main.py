from turtle import Turtle, Screen
import time
from manuelita import Manuelita
from level import Level
from obstacles import Obstacles

obstacles = Obstacles()
level = Level()
manuelita = Manuelita()
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("TURTLE CROSSING CAPSTONE PROJECT")
screen.tracer(0)
screen.listen()

screen.onkey(key="w", fun=manuelita.move_forward)
screen.onkey(key="s", fun=manuelita.move_down)

games_is_on = True

while games_is_on:
    screen.update()
    time.sleep(0.1)

    obstacles.create_car()
    obstacles.move()

    # detect when manuelita touch top
    if manuelita.ycor() >= 280:
        level.increase_level()
        manuelita.refresh()
        obstacles.increase_speed()

    # detect collision with the obstacles
    for segment in obstacles.all_cars:
        if manuelita.distance(segment) < 15:
            games_is_on = False
            level.game_is_over()

screen.exitonclick()
