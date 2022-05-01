import random
from turtle import Turtle

INITIAL_COORDINATES = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
COLORS = ["yellow", "SeaGreen1", "orange", "cyan", "maroon1", "turquoise1", "mediumpurple1"]


class Snake:
    def __init__(self):
        self.color = random.choice(COLORS)
        self.small_bit = []
        self.create_snake()
        self.head = self.small_bit[0]

    def create_snake(self):
        for coordinate in INITIAL_COORDINATES:
            self.extend(coordinate)

    def extend(self, coordinate):
        new_segment = Turtle("square")
        new_segment.color(self.color)
        new_segment.penup()
        new_segment.goto(coordinate)
        self.small_bit.append(new_segment)

    def move(self):
        for seg_num in range(len(self.small_bit) - 1, 0, -1):
            new_x = self.small_bit[seg_num - 1].xcor()
            new_y = self.small_bit[seg_num - 1].ycor()
            self.small_bit[seg_num].goto(new_x, new_y)
        self.head.forward(DISTANCE)

    def grow(self):
        self.extend(self.small_bit[-1].position())

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
