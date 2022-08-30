from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("purple")
        self.speed("normal")
        x_value = random.randint(-290, 290)
        y_value = random.randint(-290, 290)
        self.goto(x_value, y_value)
        self.new_start()

    def new_start(self):
        x_value = random.randint(-290, 290)
        y_value = random.randint(-290, 290)
        self.goto(x_value, y_value)
