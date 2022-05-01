import random
from turtle import Turtle

COLORS = ["yellow", "SeaGreen1", "orange", "cyan", "maroon1", "turquoise1", "mediumpurple1"]


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)  # makes it smaller than 20px
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.goto(self.random_location())

    def random_location(self):
        return random.randint(-280, 280), random.randint(-280, 280)
