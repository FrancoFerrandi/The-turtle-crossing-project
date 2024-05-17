from turtle import Turtle
import random

COLORS = ["red", "blue", "black", "purple", "brown", "green", "grey", "pink", "yellow", "orange"]
INCREMENT = 5
MOVE_DISTANCE = 5


class Obstacles(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.car_move = MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle()
            new_car.color(random.choice(COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.speed("fastest")
            new_car.penup()
            new_car.setheading(180)
            y_random = random.choice(range(-250, 250))
            new_car.goto(x=280, y=y_random)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.forward(self.car_move)

    def increase_speed(self):
        self.car_move += INCREMENT
        print(self.car_move)
