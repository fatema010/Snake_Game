from turtle import Turtle

INITIAL_POSITION = [(0, 0), (-20, 0), (-40, 0)]
'''here this 2 capital letter variable is called constant'''
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.start_snake = []
        self.snake_state()
        self.head = self.start_snake[0]

    def snake_state(self):
        for state in INITIAL_POSITION:
            self.add_start_snake(state)

    def add_start_snake(self, state):
        snake = Turtle("square")
        snake.color("white")
        snake.penup()
        snake.goto(state)
        self.start_snake.append(snake)
    def reset(self):
        for sn in self.start_snake:
            sn.goto(1200,1200)
        self.start_snake.clear()
        self.snake_state()
        self.head = self.start_snake[0]


    def extend(self):
        """add a new start_snake to a snake"""
        self.add_start_snake(self.start_snake[-1].position())

    def move(self):
        for label in range(len(self.start_snake) - 1, 0, -1):
            x_cor = self.start_snake[label - 1].xcor()
            y_cor = self.start_snake[label - 1].ycor()
            self.start_snake[label].goto(x_cor, y_cor)
        self.head.forward(MOVE)

    def up(self):
        if self.head.heading != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading != LEFT:
            self.head.setheading(RIGHT)
