from turtle import Turtle
FONT = ("Arial", 15, "normal")


class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(x=-200, y=260)
        self.level = 1
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align="center", font=FONT)

    def game_is_over(self):
        self.goto(x=0, y=0)
        self.write(arg=f"GAME OVER", move=False, align="center", font=('Arial', 20, 'bold'))
