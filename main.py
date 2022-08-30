import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard

from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)
snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
should_continue = True
while should_continue:
    screen.update()
    time.sleep(0.1)
    snake.move()
    # find out the collision with food
    if snake.head.distance(food) < 15:
        food.new_start()
        snake.extend()
        scoreboard.increase_score()
    # find out the collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        should_continue = False
        scoreboard.game_over()
    # find out the collision with tail
    for position in snake.start_snake[1:]:
        if snake.head.distance(position) < 10:
            should_continue = False
            scoreboard.game_over()

screen.exitonclick()
