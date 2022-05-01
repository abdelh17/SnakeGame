import time
from turtle import Screen

from board import Board
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.down, "Down")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
food = Food()
board = Board()

play = True
while play:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # find when snake eats food
    if snake.head.distance(food) < 15:
        board.update_score()
        snake.grow()
        food.goto(food.random_location())

    for bit in snake.small_bit[1:]:
        if snake.head.distance(bit) < 10:
            play = False
            board.game_over()

    if snake.head.xcor() > 285 or snake.head.xcor() < -285 or snake.head.ycor() > 285 or snake.head.ycor() < -285:
        play = False
        board.game_over()

screen.exitonclick()
