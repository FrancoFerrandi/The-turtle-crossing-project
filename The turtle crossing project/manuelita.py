from turtle import Turtle
import random

UP = 10
DOWN = 10
COLORS = ["red", "blue", "black", "purple", "brown"]


class Manuelita(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.speed("fastest")
        self.penup()
        self.setheading(90)
        self.setposition(x=0, y=-280)

    def move_forward(self):
        self.forward(UP)

    def move_down(self):
        self.back(DOWN)

    def refresh(self):
        self.color(random.choice(COLORS))
        self.setposition(x=0, y=-280)
